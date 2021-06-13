
#%%
class Restaurant:
    
    def __init__(self,restaurant_name, orders_in_line=0):
        if orders_in_line < 0:
            raise ValueError("orders_in_line should be a non-negative number.")
        
        self.restaurant_name = restaurant_name
        self.orders_in_line = orders_in_line

    def add_order_in_line(self):
        self.orders_in_line += 1

    def remove_order_in_line(self):
        if self.orders_in_line > 0:
            self.orders_in_line -= 1

    

    
# %%

Restaurant("Pizzaria d'Italia").orders_in_line


# %%
