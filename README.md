# A technical indicators library written in Python3

## General

The following indicators are available:

Standard Moving Average (SMA)

Exponential Moving Average (EMA)

Bollinger Bands

Wilder Smoothing

Relative Strength Index (RSI)

Moving Average Convergence/Divergence (MACD)

Stochastic

Stochastic RSI

Momentum

## Usage

### SMA

```python
import numpy as np
from TA import *

test = np.array([25, 24.875, 24.781, 24.594, 24.50, 24.625, 25.219, 27.25])

sma = sma(test, 5)

for x in sma:
    print(x)
```

### EMA

```python
import numpy as np
from TA import *

test = np.array([25, 24.875, 24.781, 24.594, 24.5, 24.625, 25.219, 27.25])

ema = ema(test, 10)

for x in ema:
    print(x)
```

### Bollinger Bands

```python
import numpy as np
from TA import *

test = np.array([31.875, 32.125, 32.3125, 32.125, 31.875, 32.3125, 32.25,
                     32.4375, 32.8125, 32.375, 32.5, 32.4375, 32.75, 33.1875,
                     33.0625, 33.0625, 33.125, 33.0625, 32.8125, 32.875, 33.25,
                     33.125])

lower, middle, upper = bollinger_bands(test, window=5)

for i in range(len(lower)):
    print("{:.4f}\t{:.4f}\t{:.4f}".format(middle[i], upper[i], lower[i]))
```

### Wilder Smooth

```python
import numpy as np
from TA import *

test = np.array([62.125, 61.125, 62.3438, 65.3125, 63.9688, 63.4375,
                     63, 63.7812, 63.4062, 63.4062, 62.4375, 61.8438])

wilder = wilder_smooth(test, 5)

for wild in wilder:
    print(wild)
```

### RSI

```python
import numpy as np
from TA import *

test = [37.875, 39.5, 38.75, 39.8125, 40, 39.875, 40.1875, 41.25, 41.125,
            41.625, 41.25, 40.1875, 39.9375, 39.9375, 40.5, 41.93785, 42.25,
            42.25, 41.875, 41.875]

rsi = rsi(test, window=5)

for r in rsi:
    print(r)
```

### MACD

```python
import numpy as np
from TA import *

test = np.array([63.75, 63.625, 63, 62.75, 63.25, 65.375, 66, 65, 64.875,
                     64.75, 64.375, 64.375, 64.625, 64.375, 64.5, 65.25,
                     67.875, 68, 66.875, 66.25, 65.875, 66, 65.875, 64.75,
                     63, 63.375, 63.375, 63.375])

macd, macd_signal = macd(test)

for i in range(len(macd)):
    print("{:.4f}\t{:.4f}".format(macd, macd_signal))
```
