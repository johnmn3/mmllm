# Aesop capstone — sample records

37 unique chapters across 10 fables. 27 single-call, 10 eval+answer chain.

Each record below is the raw rendered output as it would land in the byte-bin training corpus. Quad-backtick fences are used so the embedded triple-backtick clojure blocks render correctly.

---

## Example 1: ant-grasshopper / comparison-survival

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Winter lasted 51 days. Bit the ant started with 76 grains and ate 2 every day, while Skip the grasshopper started with 27 grains and ate 2 every day. If a stockpile runs out, the count cannot go below zero.

Question: How many grains does Bit have left at the end of winter?
<|end|>
<|asst|>
Time to compute the answer.

```clojure
(let [ant-stock 76
      ant-rate 2
      gh-stock 27
      gh-rate 2
      days 51
      ant-left (- ant-stock (* ant-rate days))
      gh-left (- gh-stock (* gh-rate days))]
  (max ant-left 0))
;=> 0
```

Thus, bit has 0 grains left.

{"tool_calls":[{"name":"answer","args":{"value":0}}]}
<|end|>

````

## Example 2: ant-grasshopper / summer-stockpile-days

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Through the summer at the forest, Bit the ant collected 496 grains in all, gathering 8 grains each day.

Question: How many days did Bit spend collecting?
<|end|>
<|asst|>
Let me trace through the math.

```clojure
(let [total 496
      per-day 8]
  (quot total per-day))
;=> 62
```

Then bit spent 62 days collecting.

{"tool_calls":[{"name":"answer","args":{"value":62}}]}
<|end|>

````

## Example 3: ant-grasshopper / summer-stockpile-rate

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Through the summer at the pond, Tic the ant worked steadily for 56 days and gathered 336 grains in all.

Question: How many grains did Tic collect each day?
<|end|>
<|asst|>
I divide the total by the number of days.

```clojure
(let [total 336
      days 56]
  (quot total days))
;=> 6
```

Tic collected 6 grains per day.

{"tool_calls":[{"name":"answer","args":{"value":6}}]}
<|end|>

````

## Example 4: ant-grasshopper / summer-stockpile-total

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
All summer long at the river bank, Bit the ant collected 6 grains every day for 79 days.

Question: How many grains did Bit collect by the end of summer?
<|end|>
<|asst|>
Let me think through this.

```clojure
(let [per-day 6
      days 79]
  (* per-day days))
;=> 474
```

Thus, bit collected 474 grains.

{"tool_calls":[{"name":"answer","args":{"value":474}}]}
<|end|>

````

## Example 5: ant-grasshopper / winter-consumption

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Toc the ant has 111 grains stored for winter. She eats 5 grains per day.

Question: For how many whole days will Toc's stockpile last?
<|end|>
<|asst|>
Working through this carefully.

```clojure
(let [stockpile 111
      per-day 5]
  (quot stockpile per-day))
;=> 22
```

Thus, the stockpile lasts 22 days.

{"tool_calls":[{"name":"answer","args":{"value":22}}]}
<|end|>

````

## Example 6: boy-wolf / false-alarms

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Lou kept watch over the sheep in the meadow. Bored, she shouted 'Wolf!' 2 times falsely. Each time, 9 villagers ran from the village to the field, each round trip lasting 9 minutes each.

Question: How many total minutes did the villagers waste running to 2 false alarms?
<|end|>
<|asst|>
Here's how I'd compute it.

```clojure
(let [villagers 9
      alarms 2
      minutes-per-trip 9]
  (* villagers alarms minutes-per-trip))
;=> 162
```

So the villagers wasted 162 minutes in total.

{"tool_calls":[{"name":"answer","args":{"value":162}}]}
<|end|>

````

## Example 7: boy-wolf / sheep-eaten

- code form: block
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Lou kept a flock of 63 sheep. Once the villagers had stopped believing, a hungry wolf showed up and the villagers ignored her. The wolf ate 8 sheep.

Question: How many sheep does Lou have left?
<|end|>
<|asst|>
Let me solve this step by step.

```clojure
(def flock-size 63)
(def sheep-eaten 8)
(- flock-size sheep-eaten)
;=> 55
```

{"tool_calls":[{"name":"answer","args":{"value":55}}]}
<|end|>

````

## Example 8: boy-wolf / trust-threshold

- code form: block
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
The villagers in Jess's village stop responding to alarms after 3 false alarms. So far, Jess has raised 3 false alarms.

Question: Will the villagers come on the next alarm? Answer yes or no.
<|end|>
<|asst|>
I compare alarms-so-far against the threshold; if below, villagers still come.

```clojure
(def threshold 3)
(def alarms-so-far 3)
(if (< alarms-so-far threshold) "yes" "no")
;=> "no"
```

Thus, the answer is no.

{"tool_calls":[{"name":"answer","args":{"value":"no"}}]}
<|end|>

````

## Example 9: crow-pitcher / enough-stones

- code form: block
- preface:   none
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
Korvus the crow has only 1 pebble left. The pitcher's water sits at 4 centimeters and needs to reach 18 centimeters to drink. Each pebble raises the water by 2 centimeters.

Question: Can Korvus drink with the pebbles he has? Answer with yes or no.
<|end|>
<|asst|>
```clojure
(def n-stones 1)
(def rise-per 2)
(let [start-cm 4
      target-cm 18
      reachable (+ start-cm (* n-stones rise-per))]
  (>= reachable target-cm))
;=> false
```

Then the answer is no.

{"tool_calls":[{"name":"eval","args":{"form":"(def n-stones 1)\n(def rise-per 2)\n(let [start-cm 4\n      target-cm 18\n      reachable (+ start-cm (* n-stones rise-per))]\n  (>= reachable target-cm))"}},{"name":"answer","args":{"value":false}}]}
<|end|>

````

## Example 10: crow-pitcher / stones-needed

- code form: block
- preface:   none
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
After a long flight at the meadow, Sable the crow found a pitcher of water, but the water sat only 3 centimeters from the bottom — too low to reach. They needed the water to rise to 5 centimeters before they could drink. They began dropping pebbles into the pitcher, and each pebble pushed the level up by 1 centimeter.

Question: What is the smallest number of pebbles Sable needs to drop in to reach the target water level?
<|end|>
<|asst|>
```clojure
(def rise-per-stone 1)
(def start-cm 3)
(let [target-cm 5
      level-gap (- target-cm start-cm)]
  (quot (+ level-gap (dec rise-per-stone)) rise-per-stone))
;=> 2
```

Sable needs 2 pebbles.

{"tool_calls":[{"name":"answer","args":{"value":2}}]}
<|end|>

````

## Example 11: crow-pitcher / water-rise

- code form: inline
- preface:   none
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Sable the crow spotted a pitcher with water at 4 centimeters. They tossed in 11 pebbles, and each one raised the water by 1 centimeter.

Question: After dropping all 11 pebbles, what is the new water level in centimeters?
<|end|>
<|asst|>
```clojure
(let [rise-per-stone 1
      start-cm 4
      n-stones 11]
  (+ start-cm (* n-stones rise-per-stone)))
;=> 15
```

The water level rises to 15 centimeters.

{"tool_calls":[{"name":"answer","args":{"value":15}}]}
<|end|>

````

## Example 12: dog-shadow / double-loss

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Bell the dog crossed a stream carrying 8 bones. Peering at the surface, she saw her reflection and thought it was another dog with more bones. She let go of one bone, lunging at the reflection, but the bone fell into the stream.

Question: How many bones does Bell have now?
<|end|>
<|asst|>
I subtract 1 (the dropped bone) from the original count.

```clojure
(let [start-bones 8] (dec start-bones))
;=> 7
```

Bell has 7 bones left.

{"tool_calls":[{"name":"answer","args":{"value":7}}]}
<|end|>

````

## Example 13: dog-shadow / exchange-loss

- code form: block
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Bell the dog had 8 bones. Alex offered to trade — Bell would give 3 bones in exchange for some larger ones. But the trader cheated and only gave back 2 bones.

Question: How many bones does Bell have after the trade?
<|end|>
<|asst|>
I subtract given, then add received back to the start.

```clojure
(def start-bones 8)
(def bones-given 3)
(def bones-received 2)
(+ (- start-bones bones-given) bones-received)
;=> 7
```

Therefore, bell ends with 7 bones.

{"tool_calls":[{"name":"answer","args":{"value":7}}]}
<|end|>

````

## Example 14: dog-shadow / regret

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Rex the dog expected to bring home 8 bones, but lost one chasing a shadow and ended up with one fewer.

Question: How many bones did Rex fall short by, compared to what he expected?
<|end|>
<|asst|>
Working through this carefully.

```clojure
(let [expected-bones 8
      actual-bones (dec expected-bones)]
  (- expected-bones actual-bones))
;=> 1
```

Rex fell short by 1 bone.

{"tool_calls":[{"name":"answer","args":{"value":1}}]}
<|end|>

````

## Example 15: fox-grapes / give-up

- code form: inline
- preface:   narrative
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
Vix the fox grew tired of jumping for the grapes. She would give up after 7 attempts. So far she had tried 0 times.

Question: Will Vix try again? Answer yes or no.
<|end|>
<|asst|>
I check whether tried is still below the threshold.

```clojure
(let [threshold 7
      tries-so-far 0]
  (if (< tries-so-far threshold) "yes" "no"))
;=> "yes"
```

The answer is yes.

{"tool_calls":[{"name":"eval","args":{"form":"(let [threshold 7\n      tries-so-far 0]\n  (if (< tries-so-far threshold) \"yes\" \"no\"))"}},{"name":"answer","args":{"value":"yes"}}]}
<|end|>

````

## Example 16: fox-grapes / jumps-needed

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
The grapes hung from a vine 12 feet above the ground. Renard the fox could leap 2 feet straight up each try, and each leap brought the grapes that much closer to reach.

Question: What is the smallest number of leaps Renard needs to reach the grapes?
<|end|>
<|asst|>
Stepping through the calculation.

```clojure
(let [grape-height 12
      per-jump 2]
  (quot (+ grape-height (dec per-jump)) per-jump))
;=> 6
```

Renard needs 6 jumps.

{"tool_calls":[{"name":"answer","args":{"value":6}}]}
<|end|>

````

## Example 17: fox-grapes / max-reach

- code form: block
- preface:   narrative
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
Vix the fox stretched up on hind paws, reaching 4 feet high, and could leap another 4 feet.

Question: What is the highest point Vix can reach with a single leap?
<|end|>
<|asst|>
I add the body-stand height and the jump height.

```clojure
(def body-height 4)
(def jump-height 4)
(+ body-height jump-height)
;=> 8
```

Vix can reach 8 feet high.

{"tool_calls":[{"name":"eval","args":{"form":"(def body-height 4)\n(def jump-height 4)\n(+ body-height jump-height)"}},{"name":"answer","args":{"value":8}}]}
<|end|>

````

## Example 18: goose-eggs / average

- code form: inline
- preface:   none
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
David kept Plume the goose, who laid these eggs on successive days: 1, 3, 2.

Question: What is the average eggs per day, rounded down to a whole number?
<|end|>
<|asst|>
```clojure
(let [daily-yields [1 3 2]
      total (reduce + daily-yields)
      days (count daily-yields)]
  (quot total days))
;=> 2
```

So the average is 2 eggs per day.

{"tool_calls":[{"name":"answer","args":{"value":2}}]}
<|end|>

````

## Example 19: goose-eggs / compounded

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Alice owned Plume the goose, who laid different numbers of eggs each day for 3 days: 4, 2, 1.

Question: How many eggs in total over the 3 days?
<|end|>
<|asst|>
Let me think through this.

```clojure
(let [daily-yields [4 2 1]] (apply + daily-yields))
;=> 7
```

Therefore, the total is 7 eggs.

{"tool_calls":[{"name":"answer","args":{"value":7}}]}
<|end|>

````

## Example 20: goose-eggs / total-yield

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
In the farm, Morgan owned Plume the goose. The goose laid 2 golden eggs every day, like clockwork. Morgan kept the goose for 7 days.

Question: How many eggs did the goose lay in total?
<|end|>
<|asst|>
I multiply the eggs per day by the number of days.

```clojure
(let [per-day 2
      days 7]
  (* per-day days))
;=> 14
```

The total is 14 eggs.

{"tool_calls":[{"name":"answer","args":{"value":14}}]}
<|end|>

````

## Example 21: goose-eggs / value-yield-coins

- code form: block
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Carol owned Quill the goose that laid 1 golden egg per day. Each egg sold for 46 coins at the market. After 20 days, Carol took the eggs to the village to sell.

Question: How many coins did Carol earn in total?
<|end|>
<|asst|>
I find total eggs first (per-day × days), then multiply by the per-egg coin value.

```clojure
(def per-day 1)
(def days 20)
(def per-egg-coins 46)
(def total-eggs (* per-day days))
(* total-eggs per-egg-coins)
;=> 920
```

Carol earned 920 coins.

{"tool_calls":[{"name":"answer","args":{"value":920}}]}
<|end|>

````

## Example 22: goose-eggs / value-yield-days

- code form: block
- preface:   none
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Henry owned Plume the goose that laid 2 golden eggs per day. Each egg sold for 21 coins. By the time Henry had earned 294 coins in total, the goose had been laying for some number of days.

Question: How many days had the goose been laying?
<|end|>
<|asst|>
```clojure
(def per-day 2)
(def per-egg-coins 21)
(def total-coins 294)
(def coins-per-day (* per-day per-egg-coins))
(quot total-coins coins-per-day)
;=> 7
```

After all that, the goose had been laying for 7 days.

{"tool_calls":[{"name":"answer","args":{"value":7}}]}
<|end|>

````

## Example 23: goose-eggs / value-yield-per-egg

- code form: block
- preface:   none
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
David owned Plume the goose that laid 1 golden egg per day. After 22 days, David took the eggs to the village and earned 902 coins in all.

Question: At what price (in coins) did each egg sell?
<|end|>
<|asst|>
```clojure
(def per-day 1)
(def days 22)
(let [total-coins 902
      total-eggs (* per-day days)]
  (quot total-coins total-eggs))
;=> 41
```

Thus, each egg sold for 41 coins.

{"tool_calls":[{"name":"eval","args":{"form":"(def per-day 1)\n(def days 22)\n(let [total-coins 902\n      total-eggs (* per-day days)]\n  (quot total-coins total-eggs))"}},{"name":"answer","args":{"value":41}}]}
<|end|>

````

## Example 24: lion-bulls / days-to-defeat

- code form: inline
- preface:   none
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Roar the lion watched 6 bulls grazing. Once they scattered, he could attack one at a time, taking 4 days per bull.

Question: How many total days does Roar need to defeat all 6 bulls?
<|end|>
<|asst|>
```clojure
(let [bulls 6
      days-per-bull 4]
  (* bulls days-per-bull))
;=> 24
```

Then roar needs 24 days.

{"tool_calls":[{"name":"answer","args":{"value":24}}]}
<|end|>

````

## Example 25: lion-bulls / divide-conquer-bool

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Roar the lion has strength 6. Each of the 5 bulls has strength 3. Together the bulls' combined strength is 15.

Question: Can Roar only defeat the bulls if they separate? Answer yes if alone-the-lion-wins-but-together-they-do-not, otherwise no.
<|end|>
<|asst|>
Time to compute the answer.

```clojure
(let [lion-strength 6
      bulls 5
      bull-strength 3
      combined-strength (* bulls bull-strength)]
  (and (> lion-strength bull-strength) (< lion-strength combined-strength)))
;=> true
```

{"tool_calls":[{"name":"answer","args":{"value":true}}]}
<|end|>

````

## Example 26: lion-bulls / remaining-after-k

- code form: block
- preface:   narrative
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
Mane the lion faced 9 bulls grazing alone in the field. After several days, she had defeated 6 of them.

Question: How many bulls remain?
<|end|>
<|asst|>
I subtract the defeated from the original count.

```clojure
(def bulls 9)
(def bulls-defeated 6)
(- bulls bulls-defeated)
;=> 3
```

There are 3 bulls left.

{"tool_calls":[{"name":"eval","args":{"form":"(def bulls 9)\n(def bulls-defeated 6)\n(- bulls bulls-defeated)"}},{"name":"answer","args":{"value":3}}]}
<|end|>

````

## Example 27: milkmaid / egg-to-coin-chain

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Margery carried a pail of milk to market and started to plan her fortune. She would buy 10 eggs; each would hatch into a hen; each hen would lay 144 eggs per year; each egg would sell for 5 coins.

Question: If everything went perfectly, how many coins would Margery earn after one year?
<|end|>
<|asst|>
I multiply eggs × eggs-per-hen-per-year × coins-per-egg to get the total.

```clojure
(let [eggs 10
      eggs-per-hen 144
      coins-per-egg 5]
  (* eggs eggs-per-hen coins-per-egg))
;=> 7200
```

Margery would earn 7200 coins in a year.

{"tool_calls":[{"name":"answer","args":{"value":7200}}]}
<|end|>

````

## Example 28: milkmaid / investment-return

- code form: block
- preface:   narrative
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
Margery bought a cow for 75 coins. The cow gives 8 cups of milk per day, and each cup sells for 2 coins.

Question: What is the smallest whole number of days until Margery fully recovers the cost of the cow?
<|end|>
<|asst|>
I find daily revenue (cups × coin-per-cup), then ceiling-divide the cow's cost by that revenue.

```clojure
(def cow-cost 75)
(def cups-per-day 8)
(let [coin-per-cup 2
      daily-revenue (* cups-per-day coin-per-cup)]
  (quot (+ cow-cost (dec daily-revenue)) daily-revenue))
;=> 5
```

After all that, it takes 5 days to break even.

{"tool_calls":[{"name":"eval","args":{"form":"(def cow-cost 75)\n(def cups-per-day 8)\n(let [coin-per-cup 2\n      daily-revenue (* cups-per-day coin-per-cup)]\n  (quot (+ cow-cost (dec daily-revenue)) daily-revenue))"}},{"name":"answer","args":{"value":5}}]}
<|end|>

````

## Example 29: milkmaid / spilled-milk

- code form: block
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Lila carried a pail with 24 cups of milk. She tripped and spilled 17 cups. Each cup of milk would have sold for 1 coin.

Question: How many coins did Lila lose by spilling?
<|end|>
<|asst|>
I multiply the spilled cups by the price per cup.

```clojure
(def spilled 17)
(def per-cup 1)
(* spilled per-cup)
;=> 17
```

Lila lost 17 coins.

{"tool_calls":[{"name":"answer","args":{"value":17}}]}
<|end|>

````

## Example 30: tortoise-hare / distance-remaining

- code form: inline
- preface:   narrative
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
In a long race across the forest, the course is 21 miles. Shelly the tortoise has already walked 11 miles. She continues at 3 miles per hour.

Question: How many more whole hours of walking does Shelly need to reach the finish line?
<|end|>
<|asst|>
Time to compute the answer.

```clojure
(let [total 21
      miles-walked 11
      walk-speed 3
      miles-remaining (- total miles-walked)]
  (quot miles-remaining walk-speed))
;=> 3
```

Then shelly needs 3 more hours of walking.

{"tool_calls":[{"name":"eval","args":{"form":"(let [total 21\n      miles-walked 11\n      walk-speed 3\n      miles-remaining (- total miles-walked)]\n  (quot miles-remaining walk-speed))"}},{"name":"answer","args":{"value":3}}]}
<|end|>

````

## Example 31: tortoise-hare / nap-overtake

- code form: block
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Once upon a time, Hopper the hare raced Slowpoke the tortoise to a race through the hilltop. Hopper claimed to be the swiftest, while Slowpoke just kept a steady pace.

After running 8 miles ahead, Hopper felt sleepy and stretched out for a nap. Meanwhile, Slowpoke kept walking at 3 miles per hour. While Hopper slept, Slowpoke walked for 7 hours straight.

Question: After Slowpoke's walk, who is in the lead?
<|end|>
<|asst|>
Let me think through this.

```clojure
(def hare-lead 8)
(def tortoise-rate 3)
(let [nap-hours 7
      tortoise-pos (* tortoise-rate nap-hours)]
  (if (> tortoise-pos hare-lead) "Slowpoke" "Hopper"))
;=> "Slowpoke"
```

{"tool_calls":[{"name":"answer","args":{"value":"Slowpoke"}}]}
<|end|>

````

## Example 32: tortoise-hare / speed-comparison-distance

- code form: block
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Pip the hare and Mossback the tortoise agreed to a steady race through the meadow. They ran at 7 miles per hour, while Mossback kept a steady 1 mile per hour. Both ran for exactly 4 hours.

Question: How many miles ahead is Pip after 4 hours?
<|end|>
<|asst|>
I'll compute each runner's distance by multiplying speed by time, then subtract.

```clojure
(def hare-speed 7)
(def tortoise-speed 1)
(def hours 4)
(def hare-distance (* hare-speed hours))
(def tortoise-distance (* tortoise-speed hours))
(- hare-distance tortoise-distance)
;=> 24
```

Pip is 24 miles ahead.

{"tool_calls":[{"name":"answer","args":{"value":24}}]}
<|end|>

````

## Example 33: tortoise-hare / speed-comparison-hours

- code form: block
- preface:   narrative
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
Whisker the hare and Shelly the tortoise agreed to a steady race through the meadow. He ran at 10 miles per hour, while Shelly plodded at 3 miles per hour. After some time, Whisker was exactly 28 miles ahead.

Question: How many hours had they been running?
<|end|>
<|asst|>
The gap grows by (hare-speed minus tortoise-speed) per hour, so I divide miles-ahead by that gap rate.

```clojure
(def hare-speed 10)
(def tortoise-speed 3)
(def miles-ahead 28)
(def gap-per-hour (- hare-speed tortoise-speed))
(quot miles-ahead gap-per-hour)
;=> 4
```

They had been running for 4 hours.

{"tool_calls":[{"name":"eval","args":{"form":"(def hare-speed 10)\n(def tortoise-speed 3)\n(def miles-ahead 28)\n(def gap-per-hour (- hare-speed tortoise-speed))\n(quot miles-ahead gap-per-hour)"}},{"name":"answer","args":{"value":4}}]}
<|end|>

````

## Example 34: tortoise-hare / speed-comparison-speed

- code form: block
- preface:   narrative
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
Hopper the hare and Slowpoke the tortoise agreed to a steady race through the meadow. Slowpoke kept a steady 3 miles per hour. Both ran for exactly 4 hours, by the end of which Hopper was 16 miles ahead.

Question: What was Hopper's speed in miles per hour?
<|end|>
<|asst|>
Time to compute the answer.

```clojure
(def tortoise-speed 3)
(def hours 4)
(def miles-ahead 16)
(def tortoise-distance (* tortoise-speed hours))
(def hare-distance (+ miles-ahead tortoise-distance))
(quot hare-distance hours)
;=> 7
```

Hopper's speed was 7 miles per hour.

{"tool_calls":[{"name":"eval","args":{"form":"(def tortoise-speed 3)\n(def hours 4)\n(def miles-ahead 16)\n(def tortoise-distance (* tortoise-speed hours))\n(def hare-distance (+ miles-ahead tortoise-distance))\n(quot hare-distance hours)"}},{"name":"answer","args":{"value":7}}]}
<|end|>

````

## Example 35: two-mice / food-comparison

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Squeak the mouse made a home out in the meadows and had 1 crumb, while Nibble the mouse made a home in the bustling city and had 2 crumbs.

Question: What is the absolute difference in crumbs between the two mice?
<|end|>
<|asst|>
I take the absolute value of the difference.

```clojure
(let [country-amt 1
      city-amt 2]
  (abs (- city-amt country-amt)))
;=> 1
```

The difference is 1 crumb.

{"tool_calls":[{"name":"answer","args":{"value":1}}]}
<|end|>

````

## Example 36: two-mice / shared-meal

- code form: inline
- preface:   narrative
- tool-call: 1-call (answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- answer(value: any) — submit the final answer (literal value or Clojure-source string that the runtime will eval)
<|end|>
<|user|>
Nibble the mouse and Squeak the mouse hosted a feast for 2 mice (counting themselves). They had 13 candies to share equally.

Question: How many whole candies does each mouse get if any leftover is set aside?
<|end|>
<|asst|>
Here's how I'd compute it.

```clojure
(let [total 13
      n-mice 2]
  (quot total n-mice))
;=> 6
```

Therefore, each mouse gets 6 candies.

{"tool_calls":[{"name":"answer","args":{"value":6}}]}
<|end|>

````

## Example 37: two-mice / trip-budget

- code form: block
- preface:   narrative
- tool-call: 2-call (eval+answer)

````text
<|sys|>
You are a tool-using assistant. Solve the problem with Clojure code, then submit your answer as a tool call.

Available tools:
- eval(form: string) — evaluate a Clojure-source string and return the result
- answer(value: any) — submit the final answer
<|end|>
<|user|>
Whisk the mouse began the journey with 27 coins. She spent 13 coins on travel and 9 coins on food.

Question: How many coins does Whisk have left?
<|end|>
<|asst|>
I subtract travel and food from the starting coins.

```clojure
(def start-coins 27)
(def travel-cost 13)
(let [food-cost 9] (- start-coins travel-cost food-cost))
;=> 5
```

Whisk has 5 coins remaining.

{"tool_calls":[{"name":"eval","args":{"form":"(def start-coins 27)\n(def travel-cost 13)\n(let [food-cost 9] (- start-coins travel-cost food-cost))"}},{"name":"answer","args":{"value":5}}]}
<|end|>

````

