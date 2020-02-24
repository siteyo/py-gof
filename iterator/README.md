# Iteratorパターン

## 概要
* AggregateクラスとIteratorクラスから成る
* Pythonの場合、組み込み関数のListがIteratorパターンになっている
* PythonだとAggregateクラスとIteratorクラスが同じクラスになる

## Aggregateクラス
* Iteratorと呼ばれるリストを作成する
* 各要素に対する処理が記載されている

## Iteratorクラス
* 次の要素を取り出すメソッド(ex. next)を持つ
* 次の要素を持っているか確認するメソッド(ex. hasNext)を持つ
