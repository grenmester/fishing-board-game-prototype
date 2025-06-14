# Fishing Board Game Prototyping Tools

## Rolling Mechanic

This is a CLI interface for simulating the rolling mechanic of the game. It
allows you the basic functionality to roll dice and draw cards.

```sh
cd cli-proto
python main.py
```

## Card Template

This allows you to generate card printouts for physical playtesting from YAML
data.

```sh
cd card-printout
typst compile cards.typ
```

## Cast Mechanic Balancing

This is a WebSocket-based web interface for simulating the casting mechanic of
the game. It allows players from different devices to connect to a server and
play together. Available features include habitats, dice rolling, and card
drawing.

```sh
# start server
cd ws-proto/server
node server.js

# start client in another window
cd ws-proto/client
pnpm dev
```
