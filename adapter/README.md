# Adapterパターン

## 概要
* 既存のクラスを修正せず、インタフェースに修正を吸収する
* やり方は2種類
    - もとのクラスを継承し、インタフェースを追加するパターン
    - もとのクラスをメンバにインスタンス化し、もとのクラスのメソッドを呼ぶメソッドを作成するパターン