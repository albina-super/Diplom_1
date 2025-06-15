
class TestDatabase:

    def test_available_buns_success(self, database, mock_bun):
        database.buns.append(mock_bun)
        buns_in_db = database.available_buns()
        assert mock_bun in buns_in_db and type(buns_in_db) == list


    def test_available_ingredients_success(self, database, mock_ingredient):
        database.ingredients.append(mock_ingredient)
        ingredients_in_db = database.available_ingredients()
        assert mock_ingredient in ingredients_in_db and type(ingredients_in_db) == list