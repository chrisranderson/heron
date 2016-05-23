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

## Church from [here](http://forestdb.org/models/linear-regression.html)
    (define xs '(0 1 2 3))
    (define ys '(0 1 4 6))
    
    (define samples
      (mh-query
    
       1000 10
    
       (define m (gaussian 0 2))
       (define b (gaussian 0 2))
       (define sigma-squared (gamma 1 1))
    
       (define (f x)
         (+ (* m x) b))
    
       m
    
       (all
        (map (lambda (x y) (equal? (gaussian (f x) sigma-squared y) y))
             xs
             ys))))
    
    (hist samples "Predicted y for x=4" #t)

## Figaro
Gave up installing.

## Probabilistic-C
Source isn't released yet.

## PyMC3 from [here](https://github.com/pymc-devs/pymc3/blob/3cf54ce12f7efc35af084f2fddff650159c9e2c2/pymc3/examples/GLM-linear.ipynb).
    with Model() as model: # model specifications in PyMC3 are wrapped in a with-statement
        # Define priors
        sigma = HalfCauchy('sigma', beta=10, testval=1.)
        intercept = Normal('Intercept', 0, sd=20)
        x_coeff = Normal('x', 0, sd=20)

        # Define likelihood
        likelihood = Normal('y', mu=intercept + x_coeff * x,
                            sd=sigma, observed=y)
    
        # Inference!
        start = find_MAP() # Find starting value by optimization
        step = NUTS(scaling=start) # Instantiate MCMC sampling algorithm
        trace = sample(2000, step, start=start, progressbar=False)

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

## Stan from the Stan Reference
    data {
        int<lower=0> N;
        vector[N] x;
        vector[N] y;
    }
    parameters {
        real alpha;
        real beta;
        real<lower=0> sigma;
    }
    model {
        y ~ normal(alpha + beta * x, sigma);    
    }

## Venture [from here](http://probcomp.csail.mit.edu/venture/release-0.5/tutorial/linear-regression/index.html): 
    assume intercept = normal(0,10);
    assume slope = normal(0,10)
    assume line = proc(x) { slope * x + intercept }
    assume obs = proc(x) { normal(line(x), 1) }
    
    // A tiny data set
    observe obs(1) = 2;
    observe obs(2) = 2;
    
    // Should be solvable exactly
    infer conditional;
    
    // Do we get plausible values?
    sample list(intercept, slope, line(3))

## WebPPL [from here](https://github.com/probmods/webppl/blob/master/examples/linearRegression.wppl)
    var xs = [0, 1, 2, 3]
    var ys = [0, 1, 4, 6]
    
    var model = function() {
      var m = gaussian(0, 2)
      var b = gaussian(0, 2)
      var sigmaSquared = gamma(1, 1)
    
      var f = function(x) {
        return m * x + b
      }
    
      map2(
          function(x, y) {
            factor(gaussianERP.score([(f(x)), sigmaSquared], y))
          },
          xs,
          ys)
    
      return f(4)
    }
    
    MH(model, 10000)
    
## Heron



