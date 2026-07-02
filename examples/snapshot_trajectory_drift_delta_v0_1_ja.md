# Snapshot Trajectory / Drift Delta v0.1 日本語例

## 位置づけ

`outputs/snapshot_trajectory_drift_delta_ja.svg` は、Snapshot Trajectory / Drift Delta の静的な日本語プロトタイプです。

ここで使っている Snapshot 1-3 は固定サンプルであり、実プロジェクトの自動比較結果ではありません。

## 何を見る図か

初回の図は、現在位置を示します。

- Quest Position Map: いまどこにいるか
- Industry Slope Timeline: 参照ニッチのライフサイクル上どこにいるか
- Snapshot Trajectory / Drift Delta: 前回から何が変わったか

この図の主役は、1回の診断ではなく、複数回の As-of 記録を比べることです。

## Recurring TimeTube Value

初回チャートは一度だけ強い価値を持ちます。

しかし、プロジェクトが続くほど重要になるのは、前回からの変化です。

Snapshot Trajectory / Drift Delta は、次を見えるようにします。

- Gate は変わったか
- Evidence は増えたか
- Paid Repeat は出たか
- Risk は上がったか
- Do-Not-Do Boundary は守られたか
- Codex は正しい Gate から再開しているか
- プロジェクトは compounding / stalled / drifting / risk-escalating のどれに近いか

## 今回の固定サンプルの読み方

サンプル対象:

```text
AI低導入・反復業務圧縮
```

Snapshot 1 では、Gate は PROOF で、Output Equivalence と Paid Repeat がまだ未証明です。

Snapshot 2 では、Output Equivalence が OBSERVED になり、Paid Repeat が PARTIAL になります。これは前進ですが、まだ汎用化する段階ではありません。

Snapshot 3 では、Paid Repeat が STRONG になり、Gate は INCUBATE 候補になります。ただし、Enemy Pressure も HIGH に上がるため、READY TO ADVANCE と同時に RISK RISING です。

## Codex が読むべきこと

将来の Codex/AI は、この図を見たら次を確認します。

- 最新 Snapshot だけでなく、前回との差分を読む
- Gate が上がった理由を evidence で確認する
- Do-Not-Do Boundary が緩んでいないか見る
- next action がまだ有効か判断する
- human Seat が Gate 変更を承認しているか確認する

Codex は、trajectory label を実装許可として扱ってはいけません。

## 繰り返し説明を減らす価値

この図があると、ユーザーは毎回ゼロから説明しなくてよくなります。

Future Codex は、次のように再開できます。

```text
前回は PROOF。
今回は Paid Repeat が強くなった。
ただし Enemy Pressure も上がった。
だから INCUBATE 候補だが、platform化はまだHOLD。
次は狭い repeat package の定義。
```

これは、 uncontrolled expansion を防ぎます。

## 境界

このプロトタイプは:

- 実データではない
- 自動比較ではない
- 自動スコアリングではない
- 予測ではない
- ローンチ許可ではない
- Quest Snapshot runtime ではない
- PDF生成やスクショ自動化ではない

## Completion Line

Snapshot Trajectory / Drift Delta v0.1 Japanese example explains the static prototype as a recurring TimeTube value layer for comparing saved As-of snapshots without adding runtime comparison, automatic drift scoring, prediction, or launch permission.
