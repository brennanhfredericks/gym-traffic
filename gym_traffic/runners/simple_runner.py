import numpy as np

class SimpleRunner(object):
    def __init__(self, max_steps_per_episode = 10000):
        self.max_steps_per_episode=max_steps_per_episode

    def run(self, env, agent, nb_episodes = 100, render=True, verbose=True, train=True):
        episode_rewards = []
        for episode in range(nb_episodes):
            agent.new_episode()
            observation = env.reset()
            agent.observe(observation)
            total_reward = 0
            for t in range(10000):
                if render:
                    env.render()
                action = agent.act()
                observation, reward, done, info = env.step(action)
                reward += total_reward
                agent.observe(observation)
                if train:
                    agent.learn(action, reward)
                if done:
                    if verbose:
                        print("Episode finished after {} timesteps. Total reward: {}.".format(t, total_reward))
                    break
            if not done:
                if verbose:
                    print("Episode timed-out after {} timesteps. Total reward: {}.".format(t, total_reward))
            episode_rewards.append(total_reward)
        if verbose:
            print("Average reward: {}".format(np.mean(episode_rewards)))
        return episode_rewards