
# The Zen of Heron
- Syntax should be guessable by non-programmers.
    - (difference between what you write on paper and in code should be minimal)
- Error messages are a guide to the language.
- Language design is driven by language application.
- Concurrency is the language's problem, not the user's.
- Ease of use over ease of language implementation.
    - (what about tooling?)
    - (don't let your language design be dictated by what the parser generator can handle)

## Questions
- How closely should the language follow mathematical notation? Infix?
    - It would be nice for sampling to follow the notation
- Types? Maybe restraints like "> 0"
- Represent graphical models for you?
- Built in unit tests? Probably not.
- Plotting?
- Use of p( a| b) syntax, p(a, b)
- E(v, h) = sum(v, h)
- o<
- infix operators, prefix functions?
- somehow get data from python