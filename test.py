last_names_translated = customers.select(
    pl.col("name")
    .str.extract(r"(.+) (.+)", group_index=2)
    .map_elements(name_to_number, return_dtype=pl.String)
    .alias("name_number"),
    pl.col("name"),
    pl.col("phone"),
)

last_names_translated.filter(
    pl.col("name_number") == pl.col("phone").str.replace_all("-", "")
)
