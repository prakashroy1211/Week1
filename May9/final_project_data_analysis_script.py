import pandas as pd     # for data analysis
import matplotlib.pyplot as plt # for plotting

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None  # initialize the dataframe

    def load_data(self):
        self.df = pd.read_csv(self.file_path)
        print("Data loaded successfully.")

    def clean_data(self):
        # remove symbols in rating column, convert 'rating' column to numeric and remove rows with missing data
        self.df['rating'] = self.df['rating'].str.replace('|', '')
        self.df['rating'] = pd.to_numeric(self.df['rating'], errors='coerce')
        self.df.dropna(subset=['category', 'rating'], inplace=True) # removes the rows with missing values
        print("Data cleaned.")

    def analyze_data(self):
        # Group by category and calculate average rating
        self.avg_rating = self.df.groupby('category')['rating'].mean().sort_values(ascending=False)
        self.top_categories = self.avg_rating.head(8)
        print("Analysis completed.")

        # plot average product rating by category
    def plot_results(self):
        self.top_categories.plot(kind='bar', color='lightgreen')
        plt.title('Average Product Rating by Category')
        plt.xlabel('Product Category')
        plt.ylabel('Average Rating')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()


# Example
if __name__ == "__main__":
    analyzer = DataAnalyzer("amazon.csv") # amazon sales data from kaggle is used
    analyzer.load_data()
    analyzer.clean_data()
    analyzer.analyze_data()
    analyzer.plot_results()