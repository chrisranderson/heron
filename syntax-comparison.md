Linear regression comparison of these different languages.

- m: normal(2, 1)
- b: uniform-continuous(-5, 5)
- x: [1 2 3 4 5 6  7  8  9  10]
- y: [1 3 5 7 9 11 13 15 17 19]

m should be 2
b should be -1

## Anglican
    (defquery linear-regression [xs ys]
      (let [m (sample (normal 2 1))
            b (sample (uniform-continuous -5 5))]
        
        (map (fn [x y] 
               (observe (normal (+ (* m x) b) 1) 
                        (sample (normal y 0.1)))) 
             xs 
             ys)
        
        (predict :m m)
        (predict :b b)))
    
    (def xs [1 2 3 4 5 6 7 8 9 10])
    (def ys [1 3 5 7 9 11 13 15 17 19])
    
    (def new-dist ((conditional linear-regression :lmh) xs ys))
    (def samples (repeatedly 2000 #(sample new-dist)))
    
    (plot/histogram (map :m samples))
    (plot/histogram (map :b samples))
    
## Figaro
## Probabilistic-C
## PyMC3
## Quicksand
    qs = terralib.require("qs")
    -- Model definitionlin
    reg = qs.program(function()
        return terra()
            -- The data
            var xs = array(0.0, 1.0, 2.0, 3.0)
            var ys = array(0.0, 1.0, 4.0, 6.0)
            -- Parameters
            var m = qs.gaussian(0.0, 2.0, {struc=false})
            var b = qs.gaussian(0.0, 2.0, {struc=false})
            var v = qs.gamma(1.0, 1.0, {struc=false})
            -- Condition on all the provided data
            for i=0,4 do
                qs.gaussian.observe(ys[i], m*xs[i]+b, v)
            end
            -- Predict the value at x=4
            return m*4.0 + b
        end
    end)
    -- Query the model for the MAP prediction
    queryfn = qs.infer(linreg, qs.MAP,qs.MCMC(qs.TraceMHKernel()))
    print(queryfn())
    -- output: 8.024

## Stan
## Venture
## WebPPL

## Heron



