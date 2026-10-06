"""Prueba de humo: descarga un partido de StatsBomb Open Data y dibuja sus tiros."""
import warnings
import matplotlib.pyplot as plt
from statsbombpy import sb
from mplsoccer import Pitch

warnings.filterwarnings("ignore", module="statsbombpy")  # aviso de "sin credenciales"

comps = sb.competitions()
print(comps[["competition_id", "season_id", "competition_name", "season_name"]].head(10))

# Torneo de referencia: Mundial 2022. Si no aparece, elige otro de la tabla impresa.
wc = comps[(comps.competition_name == "FIFA World Cup") & (comps.season_name == "2022")]
comp_id, season_id = int(wc.competition_id.iloc[0]), int(wc.season_id.iloc[0])

matches = sb.matches(competition_id=comp_id, season_id=season_id)
match = matches.iloc[0]  # cualquier partido vale para la prueba
events = sb.events(match_id=int(match.match_id))
shots = events[events.type == "Shot"].copy()
print(f"{match.home_team} vs {match.away_team} | eventos: {len(events)} | tiros: {len(shots)}")

pitch = Pitch(pitch_type="statsbomb")
fig, ax = pitch.draw(figsize=(10, 7))
pitch.scatter(shots.location.str[0], shots.location.str[1],
              s=shots.shot_statsbomb_xg.fillna(0.02) * 800 + 30, ax=ax)
ax.set_title(f"{match.home_team} vs {match.away_team} · tiros (tamaño = xG)")
fig.text(0.99, 0.01, "Data: StatsBomb", ha="right", fontsize=8)
fig.savefig("figures/00_smoke_test.png", dpi=150, bbox_inches="tight")
print("OK: figures/00_smoke_test.png")