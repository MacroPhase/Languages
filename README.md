# MacroPhase Language Packs

Translations live at [github.com/MacroPhase/Languages](https://github.com/MacroPhase/Languages). The app fetches them at runtime — PR merged = users get it, no app update needed.

## Quick start — New language

1. Copy [`_keys.json`](https://raw.githubusercontent.com/MacroPhase/Languages/main/_keys.json) to `<bcp47>.json`
2. Translate values (not keys). Keep placeholders (`%1$s`, `%1$d`, `%1$.1f`) as-is
3. Add your language to `_manifest.json`
4. Open a PR on [github.com/MacroPhase/Languages](https://github.com/MacroPhase/Languages)

Easiest way: paste the JSON into an AI — *"Translate these fitness app strings to [language], keep placeholders, return valid JSON."* Review, fix anything that sounds off, PR.

## Quick start — Update existing language

Open the file on GitHub, edit in-browser, commit.

**App-assisted:** Settings → Language → tap your language → **Copy missing keys** copies only the untranslated keys. Paste into AI, translate, append to the file, commit.

**In-app:** Settings → Language → long-press your language → translate key by key. Copy the translated keys using the copy button, append to file, commit.

## File format

Flat JSON. Keys must match `_keys.json` exactly.

```json
{
  "common_cancel": "Cancelar",
  "common_save": "Salvar"
}
```

| Rule | Why |
|---|---|
| Don't rename keys | The app looks up by key name |
| Don't touch placeholders | `%1$s` must stay `%1$s` — not `%s`, not `{0}` |
| Don't translate emoji | Emoji are baked into the values |
| Missing keys = English fallback | Leave them out, no breakage |

## _manifest.json

```json
{"tag": "pt-BR", "nativeName": "Português (Brasil)", "englishName": "Portuguese (Brazil)"}
```

| Field | What it is |
|---|---|
| `tag` | BCP-47 tag, must match filename |
| `nativeName` | Shown in the language picker |
| `englishName` | Subtitle in the picker |
