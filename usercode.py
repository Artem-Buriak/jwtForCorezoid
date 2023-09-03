import jwt
from cryptography.hazmat.primitives import serialization


def handle(data):
    payload_data = {
        "iat": 1696083454,
        "exp": 1696083454,
        "jti": "d793ccbb",
        "application_id": "ba6a8954-46aa-4f7e-beda-7c77ed718285"
    }
    
    key = """-----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDxYkwwy+8tbQIn
    fQDY0NrzSGQ+jFiZV0Wo+2b4vOCBob5DTNnyKQPrE51NaLAiBfJXB683PaVRKFPB
    C8su0p6LUJQwbDYcihZ/4/strwYPywNDWd1aRgCT9KkL53yonOOnKBiqJUJOFlxd
    CEc3tFGPcvbNZ1iFPbYFHMJFLPyaVLUfNZLmHY7UKBpwEX2jVR2eiq+mD9xrbGxg
    GczcUZfKLDHLCbBDZwhTsyn1hAuwOYzK8y1sneJmDzaPOekYCjTaKCzmh1ibtMsQ
    K5C9wekB2XZMgt0zXFOKvX0dnzquIwIBaBxjLEUkpOrk3uh1QcmG3l4nU+ayw3va
    GCv/YoshAgMBAAECggEAHiOu7bzY/WwKA9I449mYLR5R3fl6KpNaEFJrtg0nXyhJ
    8G9NG06Bvb1yO7Mhou3pJ3K/Lv+Uf8CwTH9jfFIyF6UVC8LHMuMPEiLuPvMGp7wq
    iSNUXyw0cETxQppB12/XgQyhn8UNNWDXYYpiEhOCx42MQXNw+xoMezDvFOIcHEzP
    RaIGZK5GbszxRQoonIuSOAgI0mzE0svJluF6YrIxBC1vUJr9y09PmxxL0fIZTqDI
    6VXR/8sGBwcuaHKUMhXGLYx9+29SoSw1EVaGCpwtnGhEd8PA0qwYb5uGAM9zk66V
    M6yz4MVv6e6bxj3dElsFgF4gBa7pFiTh4VQrUdtpQQKBgQD9lpyebOsAdMlYhbWe
    gRYeL0fn1nFvM3ntbSFL0XIOpBGFj6CkUv64SzLW1wJZwYzRv16ZeVfmjFu3tTbm
    +BPlV0hbrd9rgn7/1YtK5kI8DgvEN7ps5oK4+4uQBmTggwAP6Brrage2Bpun96Ky
    Qc+KxpR3AV0NkvQP/Rrq9/zmuQKBgQDzrfkXTVjgPcpPmlnxYb9lbyC3Z1ReZ0Lq
    e953ltJHuMBO4NUfI2XQAR8IT4ghuEyzuI9fz7PMK+DwJNgo7ZBgvSLX0xjsXQot
    CcXNXItWdsuCdyJU4bwhZ38V6AlxUJQy4XZAGZsq/uxVI45izj0I7gnB/Qvg4Y4p
    UJVen4KTqQKBgQDv0yyzt5ZYjBqPmYS2LqbYTSbX3zrQTAKXxImkxqPzrL7VbYwj
    XEqByLx/6j/S2vVuuGmjA9tZsoxbJQqTTTKjxvQroDiX2IZ7NV3SrAkf+riuDXZF
    34rpnxvSTfnBSqMYaA5tbY11XLKBG/XGV+8L89oc4jE60Sv4owp+BaIsIQKBgQDS
    QbbAKHkbY7WA4gnhgRoIh86O8ZWWrzrJ4H+gaH6gbAVjChRafcyHobAJF7a6ga+N
    Ex6C6VCWRvYbv27UQcdl8UxzNS44JD93hQsrm0KPJImM1QbGftA5cnfxivk60PBO
    xsOlo3KDstpwy/E7yABaCCpbO+BX9ccYVvPLZY7hoQKBgHdkfuRiYA9PETboTbNH
    /PyBsAYCf88mn1zR77yLljDfQ+/rQp4ENbFpjBQXG+4kGs3GryHqe6MlC2ZOD6LP
    WOXLn3jMYoEQ4Y8sdJozl328UBBNqLdMcJVB0Lj+QiKAAHa1GQGPLFC4MWR3XHpl
    Yvdvh6L71LbhzVWoGgAlsoCy
    -----END PRIVATE KEY-----
    """
    
    token = jwt.encode(
        payload=payload_data,
        key=key,
        algorithm='RS256'
    )
    
    data["token"] = token
    return data
