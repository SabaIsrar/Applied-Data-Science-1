import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path):
    """
    Read data from a CSV file into a DataFrame.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: A DataFrame containing the data.
    """
    return pd.read_csv(file_path)

def create_monthly_mean(data_frame):
    """
    Create a DataFrame with monthly mean values for Visits, UniqueVisitors, and Pageviews.

    Args:
        data_frame (pd.DataFrame): Input data.

    Returns:
        pd.DataFrame: DataFrame with monthly mean values.
    """
    data_frame['date'] = pd.to_datetime(data_frame['Date'])
    monthly_mean = data_frame.groupby(data_frame['date'].dt.strftime('%Y-%m')).agg(
        {'Visits': 'mean', 'UniqueVisitors': 'mean', 'Pageviews': 'mean'}).reset_index()
    monthly_mean['Visits'] = monthly_mean['Visits'].round(2)
    monthly_mean['UniqueVisitors'] = monthly_mean['UniqueVisitors'].round(2)
    monthly_mean['Pageviews'] = monthly_mean['Pageviews'].round(2)
    return monthly_mean

def plot_line_plot(data_frame):
    """
    Create and display a line plot of monthly data.

    Args:
        data_frame (pd.DataFrame): Data for plotting.
    """
    plt.figure(figsize=(20, 10))
    date = data_frame['date']
    visits = data_frame['Visits']
    visitors = data_frame['UniqueVisitors']
    viewers = data_frame['Pageviews']

    plt.plot(date, visits, label="Monthly Average Visits")
    plt.plot(date, visitors, label="Monthly Average Visitors")
    plt.plot(date, viewers, label="Monthly Average Pageviews")

    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.title('Monthly Trends of Website Traffic')
    plt.legend()
    plt.show()

def plot_box_plot(data_frame):
    """
    Create and display a box plot of data.

    Args:
        data_frame (pd.DataFrame): Data for plotting.
    """
    plt.figure(figsize=(10, 6))
    plt.boxplot([data_frame['Visits'], data_frame['UniqueVisitors'], data_frame['Pageviews']],
                labels=['Visits', 'Visitors', 'Pageviews'], showfliers=False)
    plt.xlabel('Variables')
    plt.ylabel('Values')
    plt.title('Distribution of Website Metrics for All 12 Months')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_pie_chart(data_frame):
    """
    Create and display a pie chart of total values.

    Args:
        data_frame (pd.DataFrame): Data for plotting.
    """
    total_values = data_frame[['Visits', 'UniqueVisitors', 'Pageviews']].sum()
    plt.figure(figsize=(7, 7))
    plt.pie(total_values, labels=['Visits', 'Visitors', 'Pageviews'], autopct='%1.1f%%', colors=['yellow', 'pink', 'blue'])
    plt.title('Website Metrics Distribution for the Whole Year (2018)')
    plt.show()

if __name__ == "__main__":
    file_path = 'food_hygiene.csv'
    food_hygiene_data = read_data(file_path)
    monthly_mean_data = create_monthly_mean(food_hygiene_data)

    plot_line_plot(monthly_mean_data)
    plot_box_plot(monthly_mean_data)
    plot_pie_chart(monthly_mean_data)
