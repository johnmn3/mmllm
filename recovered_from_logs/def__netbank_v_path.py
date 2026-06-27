def netbank_v_path(prefix: str, module: str, layer: int) -> str:
    """Per-module per-layer V_net mmap path. Shared by torch + MLX + harvester."""
    return f"{prefix}.{module}.{layer}.bin"
