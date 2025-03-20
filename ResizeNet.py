'''
=================================================
coding:utf-8
@Time:      2024/10/6 15:56
@File:      ResizeNet.py
@Author:    Ziwei Wang
@Function:
=================================================
'''
class TransformerResizeNet(nn.Module):
    """
    Forward:
        1. input x  (batch_size, 1, input_dim, sequence_length);
        2. Adjust input x to (sequence_length, batch_size, input_dim), in a Transformer compliant input format;
        3. After passing through the Transformer, the output shape remains the same;
        4. Apply linear layer to map the <input_dim> to <output_dim>;
        5. Adjust output to (batch_size, 1, output_dim, sequence_length).
    """
    def __init__(self, input_dim, output_dim, num_heads, num_layers, dim_feedforward, dropout=0.1):
        super(TransformerResizeNet, self).__init__()
        self.input_dim = input_dim
        self.output_dim = output_dim
        # Transformer Encoder Layer
        encoder_layer = nn.TransformerEncoderLayer(d_model=input_dim, nhead=num_heads, dim_feedforward=dim_feedforward,
                                                   dropout=dropout)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

        # Linear layer to map input_dim to output_dim
        self.fc = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        # x shape: (batch_size, 1, input_dim, sequence_length)
        batch_size, channels, input_dim, sequence_length = x.shape
        # Reshape to (sequence_length, batch_size, input_dim)
        x = x.view(batch_size, input_dim, sequence_length)
        x = x.permute(2, 0, 1)
        # Apply Transformer Encoder
        x = self.transformer_encoder(x)
        # Apply Linear layer to map input_dim to output_dim
        x = self.fc(x)
        # Reshape back to (batch_size, channels, output_dim, sequence_length)
        x = x.permute(1, 2, 0)
        x = x.view(batch_size, channels, self.output_dim, sequence_length)
        return x