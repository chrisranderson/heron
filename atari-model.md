## Elements of an atari game
- agents
    + good
    + bad
    + neutral

- objects
    + good
    + bad
    + neutral

## Objects and classification
- Object creation, cause and effect
    + Tanks cause bullets to exist
    + How should you treat an object you've never seen?
        * don't knock it till you try?
        * better safe than sorry?

- What is an object?
    + Something that can be interacted with. Walls, but not floors (unless there is significance like falling through the floor).
        * the agent or an NPC interacting
        * How do you determine if it can be interacted with?
        * What is interaction?
            - An change in what your actions do.
    + What about lunar lander where the floor is one huge object? Does it matter if everything is considered "one" or is it okay to assume tons of small, similarly classified objects?
    + Looks different
        * size, shape, color
        * moving stuff should be noted

- How do we ascribe identity to an object? What if it changes?
    + We can probably assume some temporal constancy. Changes don't change identity.
    + Maybe you can keep track of properties over time and predict.

- Is there a hierarchy of objects?
    + Yes. Atomic objects and hierarchical structures - solider vs. army
    + Tank has ammo?

- How can they be categorized?
    + agents - can act
        * good (team), bad (enemy), neutral (bystander, own bullets)
    + objects - can be acted upon
        * good (health, weapons), bad (traps), neutral (walls)
        * non-issues (environment, non-interactables)
        * Strange issue: shooting flying objects in missile command - some destroy you, some are just for points
        * What about exploding barrels? Can be good or bad.
        * Mushrooms in centipede?
    + non-objects
        * dialog screens
        * environment (safe to ignore?)

- What if it disappears off-screen? Any type of object permanence?
    + Respawning the agent
    + Maybe things you can't see don't matter in 2d games.
    + Camera zooms in and out again - maybe something like the image stabilization techniques - make a big mental map even though you see a small part.
        * How do you know the camera is panning?
            - everything moves at the same rate
            - zooming: things get larger

- What if it hasn't appeared yet? Predictions about what agents will appear?
    + Tanks shoots a bullet from off-screen, bullets only come from tanks

- Do we need to keep track of object properties?
    + motion: velocity, acceleration, max/average speed
    + behavior: good/bad

- What other relationships should be defined between objects?
    + a uses b (unlikely for NPCs)

## Agency and cause and effect
- Are actions deterministic?
    + Yes, but we can use distributions to model uncertainty about deterministic actions until we fully understand them.

- Categorizing actions
    + chained actions
    + combos - better if repeated
    + actions that span some duration, like charging

- What is an agent?
    + Safe to assume anything that is moving? Even if it is a bullet? Need to run away either way.
    + What if you have multiple agents to control?
    + How do you even determine which agent you are?

- How do we define/categorize cause and effect relationships?
    + agent-agent (enemy attacks player)
    + agent-object-agent (tank shoots bullet hits tank)
    + chained cause and effect (charge the cannon, shoot the cannon)

## "Morality"
- What is good?
    + Whatever wins the game/gets the most points
        * Do you always know how many points you have?
    + How do you determine what is good without any experience?
        * Self-preservation
    + Could be interesting to have the agent try really single-minded strategies to learn.
    + What about inaction?

## Other

- Does modal thinking have worth?
    + Not sure - are "what if" questions worth anything?

- Is it possible to infer rules of the game? Governing laws of some kind?

- Can a cause succeed its effect?

- How do we measure certainty about any of these questions?
    + What if some of them are irrelevant and the agent is paying attention anyway?

- 3d tic-tac-toe
- basic math
- menus

## Queries
- Is that thing good or bad?
- 

## Syntax
- some sort of convolutional syntax - variables that 
- easy to handle frames / time?