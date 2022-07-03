"""
Global Deaths from Natural Disasters
------------------------------------
This example shows a proportional symbols visualization of deaths from natural disasters by year and type.
"""
# category: case studies
import altair as alt
from vega_datasets import data

source = data.disasters.url

alt.Chart(source).transform_filter(
    alt.datum.Entity != 'All natural disasters'
).mark_circle(
    opacity=0.8,
    stroke='black',
    strokeWidth=1,
    strokeOpacity=0.4
).encode(
    x=alt.X('Year:O', axis=alt.Axis(labelAngle=0)),
    y=alt.Y('Entity:N', sort=alt.EncodingSortField(field="Deaths", op="sum", order='descending')),
    size=alt.Size('Deaths:Q',
        scale=alt.Scale(range=[0, 2500]),
        legend=alt.Legend(title='Deaths')
    ),
    color=alt.Color('Entity:N', legend=None),
    tooltip=["Entity:N", "Year:O", "Deaths:Q"]
).properties(
    width=450,
    height=320,
    title="Global Deaths from Natural Disasters"
).configure_axisX(
    labelOverlap=True
).configure_view(
    stroke=None
)
