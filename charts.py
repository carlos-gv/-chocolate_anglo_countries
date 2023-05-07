import matplotlib.pyplot as plt

def generate_bar_chart(labels,values, figname='fig.png'):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()
    plt.savefig(figname)

def generate_pie_chart(labels, values, figname='figPie.png'):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct="%0.1f %%")
    ax.axis('equal')
    plt.show()
    plt.savefig(figname)

if __name__ == '__main__':
    labels = ['a','b','c']
    values = [10,45,159]
    generate_pie_chart(labels,values)