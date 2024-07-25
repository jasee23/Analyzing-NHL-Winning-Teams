# %%
# import packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import plotly.graph_objects as go
from math import pi
from sklearn.preprocessing import MinMaxScaler

# %%
# create variables for each dataset

team_23 = pd.read_csv(r"teams23-24.csv")

team_22 = pd.read_csv(r"teams22-23.csv")

team_21 = pd.read_csv(r"teams21-22.csv")

# %%
# filter each dataset, removing useless columns

columns_to_keep_dict = {
    "Info": [0, 5],
    "Offense": [12, 21, 22, 23, 24, 25, 40, 41, 42, 46, 47, 48],
    "Defense": [69, 70, 71, 72, 73, 80, 88, 89, 90, 94, 95, 96],
    "Misc": [34, 35, 36, 37, 38, 39, 82, 83, 86, 87],
    "Radar": [7, 8, 9]               # xGoalsPercentage, corsiPercentage, fenwickPercentage
}

columns_to_keep_list = [0, 5, 7, 8, 9, 12, 21, 22, 23, 24, 25, 40, 41, 42, 46, 47, 48, 69, 70, 71, 72, 73, 80, 88, 89, 90, 94, 95, 96, 34, 35, 36, 37, 38, 39, 82, 83, 86, 87]

team_23 = pd.DataFrame(team_23)
team_22 = pd.DataFrame(team_22)
team_21 = pd.DataFrame(team_21)

team_23 = team_23.iloc[:, columns_to_keep_list]
team_22 = team_22.iloc[:, columns_to_keep_list]
team_21 = team_21.iloc[:, columns_to_keep_list]

# %%
# create new variables with stats from only teams that won the cup that year

def filter_winner(data_set, team):
    filtered_data = data_set[data_set["team"] == team]
    return filtered_data

winner_23 = filter_winner(team_23, "FLA")
winner_22 = filter_winner(team_22, "VGK")
winner_21 = filter_winner(team_21, "COL")

# %%
# filter datasets into 5on5, 5on4, 4on5, other, all

def filter_situation(data_set, situation_value):
    filtered_data = data_set[data_set["situation"] == situation_value]
    return filtered_data

FLA_all_23 = filter_situation(winner_23, "all")
FLA_other_23 = filter_situation(winner_23, "other")
FLA_5on5_23 = filter_situation(winner_23, "5on5")
FLA_5on4_23 = filter_situation(winner_23, "5on4")
FLA_4on5_23 = filter_situation(winner_23, "4on5")

VGK_all_22 = filter_situation(winner_22, "all")
VGK_other_22 = filter_situation(winner_22, "other")
VGK_5on5_22 = filter_situation(winner_22, "5on5")
VGK_5on4_22 = filter_situation(winner_22, "5on4")
VGK_4on5_22 = filter_situation(winner_22, "4on5")

COL_all_21 = filter_situation(winner_21, "all")
COL_other_21 = filter_situation(winner_21, "other")
COL_5on5_21 = filter_situation(winner_21, "5on5")
COL_5on4_21 = filter_situation(winner_21, "5on4")
COL_4on5_21 = filter_situation(winner_21, "4on5")

# %%
# Concatenate all scenarios

def mergedf(FLA, VGK, COL):
    df = FLA.merge(VGK, how = "outer")
    df = df.merge(COL, how = "outer")
    return df

dfFLA_all = pd.DataFrame(FLA_all_23)
dfVGK_all = pd.DataFrame(VGK_all_22)
dfCOL_all = pd.DataFrame(COL_all_21)

df_all_all = mergedf(dfFLA_all, dfVGK_all, dfCOL_all)

dfFLA_other = pd.DataFrame(FLA_other_23)
dfVGK_other = pd.DataFrame(VGK_other_22)
dfCOL_other = pd.DataFrame(COL_other_21)

df_all_other = mergedf(dfFLA_other, dfVGK_other, dfCOL_other)

dfFLA_5on5 = pd.DataFrame(FLA_5on5_23)
dfVGK_5on5 = pd.DataFrame(VGK_5on5_22)
dfCOL_5on5 = pd.DataFrame(COL_5on5_21)

df_all_5on5 = mergedf(dfFLA_5on5, dfVGK_5on5, dfCOL_5on5)

dfFLA_5on4 = pd.DataFrame(FLA_5on4_23)
dfVGK_5on4 = pd.DataFrame(VGK_5on4_22)
dfCOL_5on4 = pd.DataFrame(COL_5on4_21)

df_all_5on4 = mergedf(dfFLA_5on4, dfVGK_5on4, dfCOL_5on4)

dfFLA_4on5 = pd.DataFrame(FLA_4on5_23)
dfVGK_4on5 = pd.DataFrame(VGK_4on5_22)
dfCOL_4on5 = pd.DataFrame(COL_4on5_21)

df_all_4on5 = mergedf(dfFLA_4on5, dfVGK_4on5, dfCOL_4on5)

# %%
# create a heat map for each scenario

def plot_offense_heatmap(df, title):
    plt.figure(figsize = (10, 8))
    sns.heatmap(df[["shotsOnGoalFor", "missedShotsFor", "blockedShotAttemptsFor", "shotAttemptsFor", "goalsFor", "lowDangerShotsFor", "mediumDangerShotsFor", "highDangerShotsFor", "lowDangerGoalsFor", "mediumDangerGoalsFor", "highDangerGoalsFor"]].corr(), annot = True, cmap = "coolwarm", fmt = ".2f")
    plt.title(title)
    plt.show()

def plot_defense_heatmap(df, title):
    plt.figure(figsize = (10, 8))
    sns.heatmap(df[["shotsOnGoalAgainst", "missedShotsAgainst", "blockedShotAttemptsAgainst", "shotAttemptsAgainst", "goalsAgainst", "savedShotsOnGoalAgainst", "lowDangerShotsAgainst", "mediumDangerShotsAgainst", "highDangerShotsAgainst", "lowDangerGoalsAgainst", "mediumDangerGoalsAgainst", "highDangerGoalsAgainst"]].corr(), annot = True, cmap = "coolwarm", fmt = ".2f")
    plt.title(title)
    plt.show()

def plot_misc_heatmap(df, title):
    plt.figure(figsize = (10, 8))
    sns.heatmap(df[["penaltiesFor", "faceOffsWonFor", "hitsFor", "takeawaysFor", "giveawaysFor", "penaltiesAgainst"]].corr(), annot = True, cmap = "coolwarm", fmt = ".2f")
    plt.title(title)
    plt.show()

plot_offense_heatmap(df_all_all, "All Situations (Offense)")
plot_offense_heatmap(df_all_other, "All Other Situations (Offense)")
plot_offense_heatmap(df_all_5on5, "5 on 5 (Offense)")
plot_offense_heatmap(df_all_5on4, "5 on 4 (Offense)")
plot_offense_heatmap(df_all_4on5, "4 on 5 (Offense)")

plot_defense_heatmap(df_all_all, "All Situations (Defense)")
plot_defense_heatmap(df_all_other, "All Other Situations (Defense)")
plot_defense_heatmap(df_all_5on5, "5 on 5 (Defense)")
plot_defense_heatmap(df_all_5on4, "5 on 4 (Defense)")
plot_defense_heatmap(df_all_4on5, "4 on 5 (Defense)")

plot_misc_heatmap(df_all_all, "All Situations (Misc)")
plot_misc_heatmap(df_all_other, "All Other Situations (Misc)")
plot_misc_heatmap(df_all_5on5, "5 on 5 (Misc)")
plot_misc_heatmap(df_all_5on4, "5 on 4 (Misc)")
plot_misc_heatmap(df_all_4on5, "4 on 5 (Misc)")

# %%
# Create function to make a radar chart w/ corsi & fenwick & xGoalsPercentage pct

def plot_radar_chart_compare(team1, league_avg_stats, team1_name, team2_name, situation, title):

    team1_situation = filter_situation(team1, situation)

    stats = ["xGoalsPercentage", "corsiPercentage", "fenwickPercentage"]

    team1_stats = team1_situation[stats].mean().values.flatten().tolist()
    team2_stats = [league_avg_stats[stat] for stat in stats]

    categories = ["xGoals%", "Corsi%", "Fenwick%"]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r = team1_stats,
        theta = categories,
        fill = "toself",
        name = team1_name
    ))
    fig.add_trace(go.Scatterpolar(
        r = team2_stats,
        theta = categories,
        fill = "toself",
        name = team2_name
    ))

    fig.update_layout(
        polar = dict(
            radialaxis = dict(
                visible = True,
                range = [0, 1]
            )),
        title = title
    )

    fig.show()

def plot_radar_chart_compare2(team1, team2, team1_name, team2_name, situation, title):

    team1_situation = filter_situation(team1, situation)
    team2_situation = filter_situation(team2, situation)

    stats = ["xGoalsPercentage", "corsiPercentage", "fenwickPercentage"]

    team1_stats = team1_situation[stats].mean().values.flatten().tolist()
    team2_stats = team2_situation[stats].mean().values.flatten().tolist()

    categories = ["xGoals%", "Corsi%", "Fenwick%"]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r = team1_stats,
        theta = categories,
        fill = "toself",
        name = team1_name
    ))
    fig.add_trace(go.Scatterpolar(
        r = team2_stats,
        theta = categories,
        fill = "toself",
        name = team2_name
    ))

    fig.update_layout(
        polar = dict(
            radialaxis = dict(
                visible = True,
                range = [0, 1]
            )),
        title = title
    )

    fig.show()

def plot_radar_chart_compare3(team1, team2, team3, team1_name, team2_name, team3_name, situation, title):

    team1_situation = filter_situation(team1, situation)
    team2_situation = filter_situation(team2, situation)
    team3_situation = filter_situation(team3, situation)

    stats = ["xGoalsPercentage", "corsiPercentage", "fenwickPercentage"]

    team1_stats = team1_situation[stats].mean().values.flatten().tolist()
    team2_stats = team2_situation[stats].mean().values.flatten().tolist()
    team3_stats = team3_situation[stats].mean().values.flatten().tolist()

    categories = ["xGoals%", "Corsi%", "Fenwick%"]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r = team1_stats,
        theta = categories,
        fill = "toself",
        name = team1_name
    ))
    fig.add_trace(go.Scatterpolar(
        r = team2_stats,
        theta = categories,
        fill = "toself",
        name = team2_name
    ))
    fig.add_trace(go.Scatterpolar(
        r = team3_stats,
        theta = categories,
        fill = "toself",
        name = team3_name
    ))

    fig.update_layout(
        polar = dict(
            radialaxis = dict(
                visible = True,
                range = [0, 1]
            )),
        title = title
    )

    fig.show()

# %%
# call functions to compare vals between three winning teams
plot_radar_chart_compare3(winner_23, winner_22, winner_21, "FLA", "VGK", "COL", "all", "Corsi, Fenwick, and xGoals Percentages (All Situations)")
plot_radar_chart_compare3(winner_23, winner_22, winner_21, "FLA", "VGK", "COL", "other", "Corsi, Fenwick, and xGoals Percentages (All Other Situations)")
plot_radar_chart_compare3(winner_23, winner_22, winner_21, "FLA", "VGK", "COL", "5on5", "Corsi, Fenwick, and xGoals Percentages (Even Strength)")
plot_radar_chart_compare3(winner_23, winner_22, winner_21, "FLA", "VGK", "COL", "5on4", "Corsi, Fenwick, and xGoals Percentages (Power Play)")
plot_radar_chart_compare3(winner_23, winner_22, winner_21, "FLA", "VGK", "COL", "4on5", "Corsi, Fenwick, and xGoals Percentages (Penalty Kill)")

# %%
# find average xGoals, corsi, fenwick vals leaguewide

def calcAvg(dataSet, column):
    total = 0
    count = 0
    for value in dataSet[column]:
        total += value
        count += 1

    if count != 0:
        average = total / count
    else:
        average = 0

    return average

xGoals_2021_all = calcAvg(filter_situation(team_21, "all"), "xGoalsPercentage")
corsi_2021_all = calcAvg(filter_situation(team_21, "all"), "corsiPercentage")
fenwick_2021_all = calcAvg(filter_situation(team_21, "all"), "fenwickPercentage")

xGoals_2021_5on5 = calcAvg(filter_situation(team_21, "5on5"), "xGoalsPercentage")
corsi_2021_5on5 = calcAvg(filter_situation(team_21, "5on5"), "corsiPercentage")
fenwick_2021_5on5 = calcAvg(filter_situation(team_21, "5on5"), "fenwickPercentage")

xGoals_2021_5on4 = calcAvg(filter_situation(team_21, "5on4"), "xGoalsPercentage")
corsi_2021_5on4 = calcAvg(filter_situation(team_21, "5on4"), "corsiPercentage")
fenwick_2021_5on4 = calcAvg(filter_situation(team_21, "5on4"), "fenwickPercentage")

xGoals_2021_4on5 = calcAvg(filter_situation(team_21, "4on5"), "xGoalsPercentage")
corsi_2021_4on5 = calcAvg(filter_situation(team_21, "4on5"), "corsiPercentage")
fenwick_2021_4on5 = calcAvg(filter_situation(team_21, "4on5"), "fenwickPercentage")


xGoals_2022_all = calcAvg(filter_situation(team_22, "all"), "xGoalsPercentage")
corsi_2022_all = calcAvg(filter_situation(team_22, "all"), "corsiPercentage")
fenwick_2022_all = calcAvg(filter_situation(team_22, "all"), "fenwickPercentage")

xGoals_2022_5on5 = calcAvg(filter_situation(team_22, "5on5"), "xGoalsPercentage")
corsi_2022_5on5 = calcAvg(filter_situation(team_22, "5on5"), "corsiPercentage")
fenwick_2022_5on5 = calcAvg(filter_situation(team_22, "5on5"), "fenwickPercentage")

xGoals_2022_5on4 = calcAvg(filter_situation(team_22, "5on4"), "xGoalsPercentage")
corsi_2022_5on4 = calcAvg(filter_situation(team_22, "5on4"), "corsiPercentage")
fenwick_2022_5on4 = calcAvg(filter_situation(team_22, "5on4"), "fenwickPercentage")

xGoals_2022_4on5 = calcAvg(filter_situation(team_22, "4on5"), "xGoalsPercentage")
corsi_2022_4on5 = calcAvg(filter_situation(team_22, "4on5"), "corsiPercentage")
fenwick_2022_4on5 = calcAvg(filter_situation(team_22, "4on5"), "fenwickPercentage")


xGoals_2023_all = calcAvg(filter_situation(team_23, "all"), "xGoalsPercentage")
corsi_2023_all = calcAvg(filter_situation(team_23, "all"), "corsiPercentage")
fenwick_2023_all = calcAvg(filter_situation(team_23, "all"), "fenwickPercentage")

xGoals_2023_5on5 = calcAvg(filter_situation(team_23, "5on5"), "xGoalsPercentage")
corsi_2023_5on5 = calcAvg(filter_situation(team_23, "5on5"), "corsiPercentage")
fenwick_2023_5on5 = calcAvg(filter_situation(team_23, "5on5"), "fenwickPercentage")

xGoals_2023_5on4 = calcAvg(filter_situation(team_23, "5on4"), "xGoalsPercentage")
corsi_2023_5on4 = calcAvg(filter_situation(team_23, "5on4"), "corsiPercentage")
fenwick_2023_5on4 = calcAvg(filter_situation(team_23, "5on4"), "fenwickPercentage")

xGoals_2023_4on5 = calcAvg(filter_situation(team_23, "4on5"), "xGoalsPercentage")
corsi_2023_4on5 = calcAvg(filter_situation(team_23, "4on5"), "corsiPercentage")
fenwick_2023_4on5 = calcAvg(filter_situation(team_23, "4on5"), "fenwickPercentage")

stats_2021_all = {
    "xGoalsPercentage": xGoals_2021_all,
    "corsiPercentage": corsi_2021_all,
    "fenwickPercentage": fenwick_2021_all
}
stats_2022_all = {
    "xGoalsPercentage": xGoals_2022_all,
    "corsiPercentage": corsi_2022_all,
    "fenwickPercentage": fenwick_2022_all
}
stats_2023_all = {
    "xGoalsPercentage": xGoals_2023_all,
    "corsiPercentage": corsi_2023_all,
    "fenwickPercentage": fenwick_2023_all
}

stats_2021_5on5 = {
    "xGoalsPercentage": xGoals_2021_5on5,
    "corsiPercentage": corsi_2021_5on5,
    "fenwickPercentage": fenwick_2021_5on5
}
stats_2022_5on5 = {
    "xGoalsPercentage": xGoals_2022_5on5,
    "corsiPercentage": corsi_2022_5on5,
    "fenwickPercentage": fenwick_2022_5on5
}
stats_2023_5on5 = {
    "xGoalsPercentage": xGoals_2023_5on5,
    "corsiPercentage": corsi_2023_5on5,
    "fenwickPercentage": fenwick_2023_5on5
}

stats_2021_5on4 = {
    "xGoalsPercentage": xGoals_2021_5on4,
    "corsiPercentage": corsi_2021_5on4,
    "fenwickPercentage": fenwick_2021_5on4
}
stats_2022_5on4 = {
    "xGoalsPercentage": xGoals_2022_5on4,
    "corsiPercentage": corsi_2022_5on4,
    "fenwickPercentage": fenwick_2022_5on4
}
stats_2023_5on4 = {
    "xGoalsPercentage": xGoals_2023_5on4,
    "corsiPercentage": corsi_2023_5on4,
    "fenwickPercentage": fenwick_2023_5on4
}

stats_2021_4on5 = {
    "xGoalsPercentage": xGoals_2021_4on5,
    "corsiPercentage": corsi_2021_4on5,
    "fenwickPercentage": fenwick_2021_4on5
}
stats_2022_4on5 = {
    "xGoalsPercentage": xGoals_2022_4on5,
    "corsiPercentage": corsi_2022_4on5,
    "fenwickPercentage": fenwick_2022_4on5
}
stats_2023_4on5 = {
    "xGoalsPercentage": xGoals_2023_4on5,
    "corsiPercentage": corsi_2023_4on5,
    "fenwickPercentage": fenwick_2023_4on5
}

# %%
# radar charts to compare respective winning team to league average stats

plot_radar_chart_compare(winner_21, stats_2021_all, "COL", "League Average 2021", "all", "Colorado Avalanche vs. League Average (2021) (All Situations)")
plot_radar_chart_compare(winner_21, stats_2021_5on5, "COL", "League Average 2021", "5on5", "Colorado Avalanche vs. League Average (2021) (Even Strength)")
plot_radar_chart_compare(winner_21, stats_2021_5on4, "COL", "League Average 2021", "5on4", "Colorado Avalanche vs. League Average (2021) (Power Play)")
plot_radar_chart_compare(winner_21, stats_2021_4on5, "COL", "League Average 2021", "4on5", "Colorado Avalanche vs. League Average (2021) (Penalty Kill)")
# %%
# filter out team highest in standings in 2021 that did not make the playoffs

loser_2021 = filter_winner(team_21, "VGK")
loser_loser_2021 = filter_winner(team_21, "MTL")

# %%
# compare 2021 winner to top team to not make playoffs

plot_radar_chart_compare2(winner_21, loser_2021, "COL", "VGK", "all", "2021 Champion vs. top team to not make playoffs (All Situations)")
plot_radar_chart_compare2(winner_21, loser_2021, "COL", "VGK", "5on5", "2021 Champion vs. top team to not make playoffs (Even Strength)")
plot_radar_chart_compare2(winner_21, loser_2021, "COL", "VGK", "5on4", "2021 Champion vs. top team to not make playoffs (Power Play)")
plot_radar_chart_compare2(winner_21, loser_2021, "COL", "VGK", "4on5", "2021 Champion vs. top team to not make playoffs (Penalty Kill)")

# %%
# introduce worst team in the league standings

plot_radar_chart_compare3(winner_21, loser_2021, loser_loser_2021, "COL", "VGK", "MTL", "all", "2021 Champion vs. top team to not make playoffs vs. bottom team in league standings (All Situations)")
plot_radar_chart_compare3(winner_21, loser_2021, loser_loser_2021, "COL", "VGK", "MTL", "5on5", "2021 Champion vs. top team to not make playoffs vs. bottom team in league standings (Even Strength)")
plot_radar_chart_compare3(winner_21, loser_2021, loser_loser_2021, "COL", "VGK", "MTL", "5on4", "2021 Champion vs. top team to not make playoffs vs. bottom team in league standings (Power Play)")
plot_radar_chart_compare3(winner_21, loser_2021, loser_loser_2021, "COL", "VGK", "MTL", "4on5", "2021 Champion vs. top team to not make playoffs vs. bottom team in league standings (Penalty Kill)")
