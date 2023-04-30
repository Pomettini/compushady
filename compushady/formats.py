R32G32B32A32_FLOAT = 2
R32G32B32A32_UINT = 3
R32G32B32A32_SINT = 4
R32G32B32_FLOAT = 6
R32G32B32_UINT = 7
R32G32B32_SINT = 8
R16G16B16A16_FLOAT = 10
R16G16B16A16_UNORM = 11
R16G16B16A16_UINT = 12
R16G16B16A16_SNORM = 13
R16G16B16A16_SINT = 14
R32G32_FLOAT = 16
R32G32_UINT = 17
R32G32_SINT = 18
R8G8B8A8_UNORM = 28
R8G8B8A8_UNORM_SRGB = 29
R8G8B8A8_UINT = 30
R8G8B8A8_SNORM = 31
R8G8B8A8_SINT = 32
R16G16_FLOAT = 34
R16G16_UNORM = 35
R16G16_UINT = 36
R16G16_SNORM = 37
R16G16_SINT = 38
D32_FLOAT = 40
R32_FLOAT = 41
R32_UINT = 42
R32_SINT = 43
D24_UNORM_S8_UINT = 45
R8G8_UNORM = 49
R8G8_UINT = 50
R8G8_SNORM = 51
R8G8_SINT = 52
R16_FLOAT = 54
D16_UNORM = 55
R16_UNORM = 56
R16_UINT = 57
R16_SNORM = 58
R16_SINT = 59
R8_UNORM = 61
R8_UINT = 62
R8_SNORM = 63
R8_SINT = 64
B8G8R8A8_UNORM = 87
B8G8R8A8_UNORM_SRGB = 91

_pixel_size = {}
_pixel_size[R32G32B32A32_FLOAT] = 16
_pixel_size[R32G32B32A32_UINT] = 16
_pixel_size[R32G32B32A32_SINT] = 16
_pixel_size[R32G32B32_FLOAT] = 12
_pixel_size[R32G32B32_UINT] = 12
_pixel_size[R32G32B32_SINT] = 12
_pixel_size[R16G16B16A16_FLOAT] = 8
_pixel_size[R16G16B16A16_UNORM] = 8
_pixel_size[R16G16B16A16_UINT] = 8
_pixel_size[R16G16B16A16_SNORM] = 8
_pixel_size[R16G16B16A16_SINT] = 8
_pixel_size[R32G32_FLOAT] = 8
_pixel_size[R32G32_UINT] = 8
_pixel_size[R32G32_SINT] = 8
_pixel_size[R8G8B8A8_UNORM] = 4
_pixel_size[R8G8B8A8_UNORM_SRGB] = 4
_pixel_size[R8G8B8A8_UINT] = 4
_pixel_size[R8G8B8A8_SNORM] = 4
_pixel_size[R8G8B8A8_SINT] = 4
_pixel_size[R16G16_FLOAT] = 4
_pixel_size[R16G16_UNORM] = 4
_pixel_size[R16G16_UINT] = 4
_pixel_size[R16G16_SNORM] = 4
_pixel_size[R16G16_SINT] = 4
_pixel_size[R32_FLOAT] = 4
_pixel_size[R32_UINT] = 4
_pixel_size[R32_SINT] = 4
_pixel_size[R8G8_UNORM] = 2
_pixel_size[R8G8_UINT] = 2
_pixel_size[R8G8_SNORM] = 2
_pixel_size[R8G8_SINT] = 2
_pixel_size[R16_FLOAT] = 2
_pixel_size[R16_UNORM] = 2
_pixel_size[R16_UINT] = 2
_pixel_size[R16_SNORM] = 2
_pixel_size[R16_SINT] = 2
_pixel_size[R8_UNORM] = 1
_pixel_size[R8_UINT] = 1
_pixel_size[R8_SNORM] = 1
_pixel_size[R8_SINT] = 1
_pixel_size[B8G8R8A8_UNORM] = 4
_pixel_size[B8G8R8A8_UNORM_SRGB] = 4
_pixel_size[D32_FLOAT] = 4
_pixel_size[D24_UNORM_S8_UINT] = 4
_pixel_size[D16_UNORM] = 2


def get_pixel_size(format):
    return _pixel_size[format]
