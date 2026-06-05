# MacroPhase Languages

Community-maintained translations for [MacroPhase](https://github.com/laringologija/OpenFactor).

The app fetches language packs from this repo at runtime. No app update needed — translations ship the moment a PR is merged.

## Adding a language

1. Fork this repo
2. Create `<bcp47>.json` — copy `_keys.json` as a starting point
3. Add your language to `_manifest.json`
4. Open a PR

That's it. The app picks up new languages automatically.

## Improving a language

Edit the `.json` file, commit, PR. Even fixing one typo helps.

## File format

One flat JSON object. Keys must match `_keys.json` exactly.

```json
{
  "common_cancel": "Cancelar",
  "common_save": "Salvar",
  "ai_welcome_title": "No que podemos focar?"
}
```

### Rules

- **Keys**: copy from `_keys.json`, don't rename them
- **Placeholders**: keep exactly as-is (`%1$s`, `%1$d`, `%1$.1f`) — the app uses these for formatted strings
- **Missing keys**: just leave them out — the app falls back to English automatically
- **File name**: must match the `tag` field in `_manifest.json`

## _manifest.json

Every language needs an entry:

```json
{"tag": "pt-BR", "nativeName": "Português (Brasil)", "englishName": "Portuguese (Brazil)"}
```

| Field | What it does |
|---|---|
| `tag` | BCP-47 language tag. Must match the file name. |
| `nativeName` | Shown to the user in their own language |
| `englishName` | Shown in the picker as a subtitle |

## Translation tips

- Use any AI to generate a first draft, then review it yourself
- Locals always beat machine translation
- Keep the tone natural — this is a fitness coach app, not a legal document
- Don't translate emoji — they're baked into the values
- Don't change the placeholders — `%1$s` must stay `%1$s`, not `%s` or `{0}`

## _keys.json

This is the English source of truth. Every translatable string in the app lives here. If a key isn't in this file, it doesn't exist. If a key is in this file but not in your language pack, the app shows the English version.
