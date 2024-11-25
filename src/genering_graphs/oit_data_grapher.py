import matplotlib.pyplot as plt
import seaborn as sns

def plot_heatmap(df, title):
    """
    Plot a heatmap for the given pivot table.

    Args:
        df (pd.DataFrame): Pivot table to plot.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(12, 8))
    sns.heatmap(df, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title(title)
    plt.xlabel('Classif2')
    plt.ylabel('Classif1')
    plt.show()

def plot_stacked_bar(df, title, xlabel, ylabel):
    """
    Plot a stacked bar chart for the given pivot table.

    Args:
        df (pd.DataFrame): Pivot table to plot.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
    """
    df.plot(kind='bar', stacked=True, figsize=(12, 8))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title='Sex')
    plt.show()

def plot_line_chart(df, title, xlabel, ylabel):
    """
    Plot a line chart for the given pivot table.

    Args:
        df (pd.DataFrame): Pivot table to plot.
        title (str): Title of the plot.
        xlabel (str): Label for the x-axis.
        ylabel (str): Label for the y-axis.
    """
    df.plot(kind='line', figsize=(12, 8))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend(title='Classif2')
    plt.show()

def plot_correlation_heatmap(corr_matrix, title):
    """
    Plot a heatmap for the correlation matrix.

    Args:
        corr_matrix (pd.DataFrame): Correlation matrix to plot.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=.5)
    plt.title(title)
    plt.show()


