import pandas as pd
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt

filepath = r"E:\vegetable_data.csv"
df = pd.read_csv(filepath)

# Sort by quantity and select top 10 for better visualization
top10 = df.sort_values('quantity(kg)', ascending=False).head(10)
x = top10['veg_name']
y = top10['quantity(kg)']
# Removed unused import of matplotlib.animation

fig, axs = plt.subplots(3, 3, figsize=(20, 16), constrained_layout=True)

# 1. Bar plot
bars = axs[0, 0].bar(range(len(x)), y, color='seagreen', alpha=0.7)
axs[0, 0].set_title('Bar Plot')
axs[0, 0].set_xlabel('Vegetable Name')
axs[0, 0].set_ylabel('Quantity (kg)')
axs[0, 0].set_xticks(range(len(x)))
axs[0, 0].set_xticklabels(x, rotation=45, ha='right')
axs[0, 0].add_patch(Rectangle((-0.5, min(y)), len(x), max(y)-min(y), fill=False, edgecolor='blue', lw=2))

# 2. Line plot
line, = axs[0, 1].plot(range(len(x)), y, marker='o', color='orange')
axs[0, 1].set_title('Line Plot')
axs[0, 1].set_xlabel('Vegetable Name')
axs[0, 1].set_xticks(range(len(x)))
axs[0, 1].set_xticklabels(x, rotation=45, ha='right')
axs[0, 1].add_patch(Rectangle((-0.5, min(y)), len(x), max(y)-min(y), fill=False, edgecolor='red', lw=2))

# 3. Scatter plot
sc = axs[0, 2].scatter(range(len(x)), y, color='purple', s=100, alpha=0.7)
axs[0, 2].set_title('Scatter Plot')
axs[0, 2].set_xlabel('Vegetable Name')
axs[0, 2].set_ylabel('Quantity (kg)')
axs[0, 2].set_xticks(range(len(x)))
axs[0, 2].set_xticklabels(x, rotation=45, ha='right')
axs[0, 2].add_patch(Rectangle((-0.5, min(y)), len(x), max(y)-min(y), fill=False, edgecolor='green', lw=2))

# 4. Pie chart
pie_wedges = axs[1, 0].pie(y, labels=x, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)[0]
axs[1, 0].set_title('Pie Chart')
axs[1, 0].add_patch(Rectangle((-1.2, -1.2), 2.4, 2.4, fill=False, edgecolor='purple', lw=2))

# 5. Horizontal bar plot
bars_h = axs[1, 1].barh(range(len(x)), y, color='teal', alpha=0.7)
axs[1, 1].set_title('Horizontal Bar Plot')
axs[1, 1].set_xlabel('Quantity (kg)')
axs[1, 1].set_ylabel('Vegetable Name')
axs[1, 1].set_yticks(range(len(x)))
axs[1, 1].set_yticklabels(x)
axs[1, 1].add_patch(Rectangle((min(y), -0.5), max(y)-min(y), len(x), fill=False, edgecolor='orange', lw=2))

# 6. Stem plot
(markerline, stemlines, baseline) = axs[1, 2].stem(range(len(x)), y, linefmt='grey', markerfmt='D', basefmt=" ")
axs[1, 2].set_xticks(range(len(x)))
axs[1, 2].set_xticklabels(x, rotation=45, ha='right')
axs[1, 2].set_xlabel('Vegetable Name')
axs[1, 2].set_ylabel('Quantity (kg)')
axs[1, 2].set_title('Stem Plot')
axs[1, 2].add_patch(Rectangle((-0.5, min(y)), len(x), max(y)-min(y), fill=False, edgecolor='brown', lw=2))

# 7. Box plot
box = axs[2, 0].boxplot(y, vert=True, patch_artist=True)
axs[2, 0].set_title('Box Plot')
axs[2, 0].set_xticklabels(['Quantity (kg)'])
axs[2, 0].add_patch(Rectangle((0.5, min(y)), 1, max(y)-min(y), fill=False, edgecolor='magenta', lw=2))

# 8. Violin plot
violin = axs[2, 1].violinplot(y, showmeans=True)
axs[2, 1].set_title('Violin Plot')
axs[2, 1].set_xticks([1])
axs[2, 1].set_xticklabels(['Quantity (kg)'])
axs[2, 1].add_patch(Rectangle((0.5, min(y)), 1, max(y)-min(y), fill=False, edgecolor='cyan', lw=2))

# 9. Histogram
hist = axs[2, 2].hist(y, bins=5, color='coral', alpha=0.7)
axs[2, 2].set_title('Histogram')
axs[2, 2].set_xlabel('Quantity (kg)')
axs[2, 2].set_ylabel('Frequency')
axs[2, 2].add_patch(Rectangle((min(y), 0), max(y)-min(y), max(hist[0]), fill=False, edgecolor='black', lw=2))

# Animation functions for each subplot
def animate_bar(event):
    for bar in bars:
        bar.set_color('gold' if bar.contains(event)[0] else 'seagreen')
        bar.set_alpha(1.0 if bar.contains(event)[0] else 0.7)
    fig.canvas.draw_idle()

def animate_line(event):
    if axs[0, 1].contains(event)[0]:
        line.set_linewidth(4)
        line.set_color('red')
    else:
        line.set_linewidth(2)
        line.set_color('orange')
    fig.canvas.draw_idle()

def animate_scatter(event):
    cont, ind = sc.contains(event)
    if cont:
        sc.set_sizes([300 if i in ind['ind'] else 100 for i in range(len(x))])
    else:
        sc.set_sizes([100]*len(x))
    fig.canvas.draw_idle()

def animate_pie(event):
    for wedge in pie_wedges:
        wedge.set_alpha(1.0 if wedge.contains(event)[0] else 0.7)
        wedge.set_radius(1.1 if wedge.contains(event)[0] else 1.0)
    fig.canvas.draw_idle()

def animate_barh(event):
    for bar in bars_h:
        bar.set_color('yellow' if bar.contains(event)[0] else 'teal')
        bar.set_alpha(1.0 if bar.contains(event)[0] else 0.7)
    fig.canvas.draw_idle()

def animate_stem(event):
    # markerline is a Line2D object, not iterable
    if markerline.contains(event)[0]:
        markerline.set_markerfacecolor('red')
    else:
        markerline.set_markerfacecolor('C0')
    fig.canvas.draw_idle()

def animate_box():
    # box['boxes'] is a list of Patch objects, but Patch does not have contains(event)
    for patch in box['boxes']:
        patch.set_facecolor('lime')
    fig.canvas.draw_idle()

def animate_violin():
    # violin['bodies'] are PolyCollection, which do not have contains(event)
    for body in violin['bodies']:
        body.set_facecolor('pink')
    fig.canvas.draw_idle()

def animate_hist(event):
    for rect in axs[2, 2].patches:
        if hasattr(rect, 'contains') and rect.contains(event)[0]:
            rect.set_facecolor('blue')
        else:
            rect.set_facecolor('coral')
    fig.canvas.draw_idle()

# Connect hover events to each subplot
def on_move(event):
    if event.inaxes == axs[0, 0]:
        animate_bar(event)
    elif event.inaxes == axs[0, 1]:
        animate_line(event)
    elif event.inaxes == axs[0, 2]:
        animate_scatter(event)
    elif event.inaxes == axs[1, 0]:
        animate_pie(event)
    elif event.inaxes == axs[1, 1]:
        animate_barh(event)
    elif event.inaxes == axs[1, 2]:
        animate_stem(event)
    elif event.inaxes == axs[2, 0]:
        animate_box()
    elif event.inaxes == axs[2, 1]:
        animate_violin()
    elif event.inaxes == axs[2, 2]:
        animate_hist(event)

# Connect the hover event to the figure
fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()
