from algs.basic_sort import BasicSort
import matplotlib.pyplot as plt
import matplotlib.colors as mp_colors
from matplotlib import animation


class AlgAnimation(object):
    def __init__(self, alg: BasicSort, speed: int = 50):
        self.fig = plt.figure()
        self.steps = alg.calc_all_steps()

        data_normalizer = mp_colors.Normalize()
        color_map = mp_colors.LinearSegmentedColormap(
            "my_map",
            {
                "red": [(0, 1.0, 1.0),
                        (1.0, .5, .5)],
                "green": [(0, 0.5, 0.5),
                          (1.0, 0, 0)],
                "blue": [(0, 0.50, 0.5),
                         (1.0, 0, 0)]
            }
        )
        ax = self.fig.add_axes([0, 0, 1, 1])
        self.rects = ax.bar(range(len(alg.array)), alg.array.copy(), align="edge",
                            color=color_map(data_normalizer(range(len(alg.array)))))

        self.anim = animation.FuncAnimation(self.fig, func=self.animate, frames=self.steps,
                                            interval=speed, blit=True, repeat=False)

    def animate(self, state):
        for rect, val in zip(self.rects, state):
            rect.set_height(val)
        return self.rects

    def show(self):
        plt.show()
