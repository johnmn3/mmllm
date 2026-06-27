"""Byte-sequence markers for FIM (Fill-in-the-Middle) training.

We're a byte-level model — no vocab change is needed. Multi-byte escape
sequences (same convention as our existing `<|user|>`, `<|asst|>`,
`<|end|>`) act as FIM delimiters. The model learns to recognize them
during training because they appear at structural positions in the
training data.

11 bytes each. PSM/SPM order is decided by the corpus generator; the
training step doesn't need to know which mode was used."""

FIM_PRE: bytes = b"<|fim_pre|>"
FIM_SUF: bytes = b"<|fim_suf|>"
FIM_MID: bytes = b"<|fim_mid|>"
FIM_EOM: bytes = b"<|fim_eom|>"

ALL_FIM_MARKERS: tuple[bytes, ...] = (FIM_PRE, FIM_SUF, FIM_MID, FIM_EOM)

assert all(len(m) == 11 for m in ALL_FIM_MARKERS), \
    "FIM markers must be 11 bytes for predictable budget accounting"
