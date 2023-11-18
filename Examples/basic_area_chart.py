from sjvisualizer import plot as plt

colors = {
    "United States": [
        23,
        60,
        154
    ],
	"Russia": [
        255,
        50,
        50
    ]
}

plt.stacked_area(excel="data/Nuclear.xlsx",
        title="Nuclear Warheads by Country",
        record=True,
        output_video="Nuclear Warheads by Country.mp4",
        colors=colors)