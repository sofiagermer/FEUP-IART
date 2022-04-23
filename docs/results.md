# Results

## Simulated Annealing

### 1. (old data parameters)
![](images/Figure_1.png)

- **Light change odd:** 50
- **Light variation amplitude:** 3
- **Temperature**: simulation.points_per_car * 5
- **Cooling**: 0.7
- **Runs per temperature**: 30
- **Stop criteria**: self.temperature > self.init_temperature/1000


### Marathon 1.
- **Light change odd:** 50
- **Light variation amplitude:** 3
- **Temperature**: 1000
- **min_Temperature**: 0.1
- **max iterations**: 1000
- **Runs per temperature**: 1
- **Starting solution**: +/- 374 cars

#### Exponential cooling

![](images/sim-annealing/run1expcooling.png)
![](images/sim-annealing/run1expcoolingresults.png)


#### Logarithmic cooling

![](images/sim-annealing/run1logcooling.png)
![](images/sim-annealing/run1logcoolingresults.png)

#### Linear cooling

![](images/sim-annealing/run1lincooling.png)
![](images/sim-annealing/run1lincoolingresults.png)

#### Quadratic cooling

![](images/sim-annealing/run1quacooling.png)
![](images/sim-annealing/run1quacoolingresults.png)

#### Observations

- Starting temperature was too low


### Marathon 2.
- **Light change odd:** 50
- **Light variation amplitude:** 3
- **Temperature**: 3000
- **min_Temperature**: 0.1
- **max iterations**: 1000
- **Runs per temperature**: 1
- **Starting solution**: 375 cars (347279 points)

#### Exponential cooling

![](images/sim-annealing/run2expcooling.png)
(too cold)
![](images/sim-annealing/run2expcoolingresults.png)


#### Logarithmic cooling

![](images/sim-annealing/run2logcooling.png)
![](images/sim-annealing/run2logcoolingresults.png)

#### Linear cooling

![](images/sim-annealing/run2lincooling.png)
![](images/sim-annealing/run2lincoolingresults.png)

#### Quadratic cooling

![](images/sim-annealing/run2quacooling.png)
![](images/sim-annealing/run2quacoolingresults.png)

#### Observations

- Selection of worst solution was more visible, specially in the logarithmic cooling, however it still isn't frequent.

- Linear cooling was the best one

### Marathon 3.
- **Light change odd:** 50
- **Light variation amplitude:** 3
- **Temperature**: 5000
- **min_Temperature**: 0.1
- **max iterations**: 1000
- **Runs per temperature**: 1
- **Starting solution**: 374 cars (353178 points)

#### Exponential cooling

![](images/sim-annealing/run3expcooling.png)
![](images/sim-annealing/run3expcoolingresults.png)


#### Logarithmic cooling

![](images/sim-annealing/run3logcooling.png)
![](images/sim-annealing/run3logcoolingresults.png)

#### Linear cooling

![](images/sim-annealing/run3lincooling.png)
![](images/sim-annealing/run3lincoolingresults.png)

#### Quadratic cooling

![](images/sim-annealing/run3quacooling.png)
![](images/sim-annealing/run3quacoolingresults.png)

#### Observations

- Logarithmic cooling went nuts
- Progression in other cooling methods remained the same