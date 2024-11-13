# cargo_shop

## Description

```
你会使用 Rust 算数吗?
```

Flag: `0xGame{Rewrite_GoShop_in_Rust_cd57122cfed3}`

## Writeup

考点: 整数溢出 & release 模式

`cargo install` 在编译 crate 的时候使用的是 release 模式, 和 `cargo build --release` 类似

Rust 在 release 模式下**不**检测整数溢出, 而是会按照补码循环溢出的规则处理 (例如变量范围位于 `-128 - 127`, 那么 `127 + 1` 的结果会是 `-128`)

purchase 函数

```rust
#[get("/purchase/{name}/{count}")]
async fn purchase(info: web::Path<(String, u32)>, session: Session) -> Result<String> {
    let Some(mut user) = session.get::<User>("user")? else {
        return Ok("user not found".to_string());
    };

    let (name, count) = info.into_inner();

    let Some(goods) = GOODS_LIST.iter().find(|v| v.name == name) else {
        return Ok("goods not found".to_string());
    };

    let costs = (goods.prize * count) as i32;

    if costs <= user.balance {
        user.balance -= costs;

        if let Some(hold) = user.holds.iter_mut().find(|v| v.goods.name == goods.name) {
            hold.inventory += count;
        } else {
            user.holds.push(Hold {
                goods: goods.clone(),
                inventory: count,
            });
        }

        session.insert("user", user)?;
        Ok(format!("purchase {} x {} success", name, count))
    } else {
        Ok(format!("you don't have enough balance"))
    }
}
```

其中如下的语句

```rust
let costs = (goods.prize * count) as i32;
```

goods.prize 和 count 都是 u32 类型, 最终计算的 costs 是 i32 类型, 在强制类型转换的情况下会出现整数溢出的风险

经过搜索得知 Rust i32 的范围为 `-2147483648 ~ 2147483647`, 于是很容易构造出如下的 payload

```
http://cargoshop.challenge.exp10it.io/purchase/tokio/203333333
```

请求之后会发现 balance 变成非常大, 然后再购买一次 flag 商品即可得到 flag

```
http://cargoshop.challenge.exp10it.io/purchase/flag/1
http://cargoshop.challenge.exp10it.io/flag
```
