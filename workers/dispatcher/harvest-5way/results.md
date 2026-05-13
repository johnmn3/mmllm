# 5-way FedAvg harvest of 4 worker chain extensions

Each of 4 workers extended the dispatcher's 10-round chain by 10 more
rounds via `scripts/extend_chain.sh`, starting from
`workers/dispatcher/spork-chain-10/round-10/`. They published their
round-20 endpoints to their own `claude/sporkchain-*-extend10` branches.

Harvest: FedAvg the 4 round-20 V_nets (32 layers each) and dense.pt
into a single set of artifacts. V_local is left Gaussian-fresh (inf
mode doesn't train it).

## Worker endpoints (individual round-20 ctrl_bpc)

| handle         | branch                                          | round-20 ctrl_bpc |
|----------------|-------------------------------------------------|------------------:|
| opus47-may13   | claude/sporkchain-opus47-may13-extend10         | 1.2260 |
| round11to20    | claude/sporkchain-round11to20-extend10          | 1.2241 |
| claude-ext     | claude/sporkchain-claude-ext-extend10           | 1.2231 |
| opus47         | claude/sporkchain-opus47-extend10               | 1.2245 |

## State similarity (pairwise across the 4 workers)

| component         | cos (pairwise mean) | range          |
|-------------------|--------------------:|---------------:|
| dense.pt          | 0.9936              | 0.9921–0.9948 |
| V_net layer 0     | 0.7735              | 0.7478–0.7934 |
| V_net layer 12    | 0.8394              | 0.8315–0.8430 |
| V_net layer 31    | 0.6988              | 0.6682–0.7297 |

Dense converged tight (all 4 workers' dense.pt within ~6% of each
other). V_net diverged more — workers explored different basins in
NetBank's value space.

## Harvested vs individual

| state                                | ctrl_bpc | ppl    |
|--------------------------------------|---------:|-------:|
| dispatcher round-10 (start state)    |   1.5991 | 3.03   |
| best individual worker round-20      |   1.2231 | 2.40   |
| mean individual worker round-20      |  ~1.2244 | ~2.39  |
| **5-way FedAvg harvested**           | **1.1764** | **2.26** |

**Headline:** FedAvg of 4 parallel round-20 chains beats every individual
worker by **0.046 bpc / 6% perplexity reduction**. From the
dispatcher's round-10 starting point this is a **26% bpc reduction**
across 10 effective rounds (the extension was 10 rounds; the harvest
combines 4 such extensions into a single consensus end-state).

## Inf-spork TPS on the harvested state

cpu-mini, MMLLM_ENABLE_PKM_CPP=true:

  B=1  pure-Python:  38.87 tok/s  ( 25.7 ms/tok)
  B=16 pure-Python: 390.96 tok/s  ( 40.9 ms/tok agg)
