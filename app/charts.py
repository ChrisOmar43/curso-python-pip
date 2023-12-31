import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()

if _name_ == '_main_':
    labels = ['a', 'b', 'c']
    values = [10, 40, 800]
    # generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)