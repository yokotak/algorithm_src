import perfplot
import crc32, crc32_table

pp = perfplot.live(
    setup=lambda n: bytes('@' * n, encoding='utf-8'),
    n_range=[k for k in range(1, 100)],
    kernels=[
        crc32.crc32,
        crc32_table.crc32,
    ],
    labels=[
        'crc32.crc32',
        'crc32_table.crc32'
    ])


