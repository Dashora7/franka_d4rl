import gym
import d4rl
from envs.kitchen import KitchenEnv
import imageio
import time

t_start = time.time()
env = KitchenEnv()
env.reset()
done = False
imgs = []
for i in range(150):
    a = env.action_space.sample()
    o, r, d, i = env.step(a)
    im = o['image']
    imgoal = o['image_goal']
    # print("microwave", i["microwave distance to goal"])
    # im = env.render(mode="rgb_array")
    imgs.append(im)
print("time:", time.time() - t_start)
imageio.mimsave('out.gif', imgs)
imageio.mimsave('out_goal.gif', [imgoal]*len(imgs))

