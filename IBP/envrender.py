import gym
import matplotlib.pyplot as plt

env = gym.make('PongNoFrameskip-v4')
env.reset()

for frame_idx in range(2000):
    env.step(env.action_space.sample())
    env.render()
    # img = env.render(mode='rgb_array')
    # # plt.imshow(img)
    # # plt.show()
    # print(img.shape)
    if frame_idx % 100 == 0:
        # import pdb;pdb.set_trace()
        # img = env.render(mode='rgb_array')
        # state_img = Image.fromarray(img)
        # state_img.save('{}/{}_ori_action_{}_adv_action_{}.png'.format(prefix, frame_idx, action, adv_action))
        # if frame_idx == 20:
        #     return
        env.env.ale.saveScreenPNG('{}.png'.format(frame_idx))

env.close()
