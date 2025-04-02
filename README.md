# Scoreboard for SYIC

Prerequisites:
Install python packages from `requirements.txt`.

Usage:

create `token.json` file with format:
```json
{
  "TokenId": "xxx",
  "Token": "xxxxxxxxxxxx"
}
```
then create `config.json` file with format:
```json
{
  "problems": ["I011", "I012", "I013"]
}
```

Then run `python -m http.server` from terminal from the current directory.
Then run `write.py`.
