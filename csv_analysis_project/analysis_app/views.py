import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from django.shortcuts import render
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            df = pd.read_csv(file)

            # Store the DataFrame in session as JSON
            request.session['data'] = df.to_json()

            # Redirect to the results page
            return show_results(request)
    else:
        form = UploadFileForm()
    return render(request, 'analysis_app/upload.html', {'form': form})

def show_results(request):
    data_json = request.session.get('data')
    df = pd.read_json(data_json)

    # Basic data analysis
    first_rows = df.head().to_html()
    stats = df.describe(include='all').to_html()

    # Handle missing values
    missing_values = df.isnull().sum().to_frame().to_html()

    # Generate plots for numeric columns only
    numeric_df = df.select_dtypes(include=[np.number])
    hist_img = create_histogram(numeric_df)
    heatmap_img = create_heatmap(numeric_df)

    return render(request, 'analysis_app/results.html', {
        'first_rows': first_rows,
        'stats': stats,
        'missing_values': missing_values,
        'hist_img': hist_img,
        'heatmap_img': heatmap_img
    })

def create_histogram(df):
    img = io.BytesIO()
    df.hist()
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url

def create_heatmap(df):
    img = io.BytesIO()
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.tight_layout()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return plot_url
