# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.read_csv('./archive/FRvideos.csv')

df.loc[df['category_id'] ==1, 'category'] = 'Film & Animation'
df.loc[df['category_id'] ==2, 'category'] = 'Autos & Vehicles'
df.loc[df['category_id'] ==10, 'category'] = 'Music'
df.loc[df['category_id'] ==15, 'category'] = 'Pets & Animals'
df.loc[df['category_id'] ==17, 'category'] = 'Sports'
df.loc[df['category_id'] ==19, 'category'] = 'Travel & Events'
df.loc[df['category_id'] ==20, 'category'] = 'Gaming'
df.loc[df['category_id'] ==22, 'category'] = 'People & Blogs'
df.loc[df['category_id'] ==23, 'category'] = 'Comedy'
df.loc[df['category_id'] ==24, 'category'] = 'Entertainment'
df.loc[df['category_id'] ==25, 'category'] = 'News & Politics'
df.loc[df['category_id'] ==26, 'category'] = 'Howto & Style'
df.loc[df['category_id'] ==27, 'category'] = 'Education'
df.loc[df['category_id'] ==28, 'category'] = 'Science & Technology'
df.loc[df['category_id'] ==29, 'category'] = 'Nonprofits & Activism'


top10channel = df.groupby("channel_title").sum().sort_values("views", ascending = False).head(10)

fig = px.bar(x=top10channel.views, y=top10channel.index, color=top10channel.views)


top_video = df.groupby("title").sum().sort_values("views", ascending=False).head(10)
#fig2 = px.bar(x=top_video.view_count, y=top_video.title,  color=top_video.view_count)
fig2 = px.bar(x=top_video.views, y=top_video.index, color=top_video.views)

top_category = df.groupby("category").sum().reset_index().sort_values("views", ascending=False).head(10)
fig3 = px.bar(y=top_category.views, x=top_category.category)


category_group = df.groupby("category").sum().sort_values("comment_count", ascending=False)
fig4 = px.scatter(category_group, x="likes", y="dislikes",
	         size="views", color=category_group.index,
                 log_x=True, size_max=60)

fig5 = px.bar(category_group, x=category_group.index, y=["comment_count"], color=category_group.index)

#fig2.update_layout(
#    plot_bgcolor=colors['background'],
#    paper_bgcolor=colors['background'],
#    font_color=colors['text']
#)



app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Trending Youtube Channels',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Top 10 Trending Youtube Channels', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-1',
        figure=fig2
    ),
    html.Div(children='Top 10 Videos', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    ),
    
    html.Div(children='Top Category', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-3',
        figure=fig3
    ),
     
    html.Div(children='Likes and Dislikes by Category', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-4',
        figure=fig4
    ),
    html.Div(children='Comments by Category', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-5',
        figure=fig5
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
