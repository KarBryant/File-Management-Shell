import functools

def ascii_box(type=None):
    def decorator(funct):
        @functools.wraps(funct)
        def wrapper(*args, **kwargs):
            max_width = 60
            offset = 5

            def create_edges(max_width,offset):

               return f"*{"-"*((offset*2)+max_width) }*"

            result = funct(*args, **kwargs)
        
            def wrap_line(result_string):
            

                scraped_line = result_string[:max_width]

                if len(scraped_line) == max_width:

                    print(f"*{" "*offset}{scraped_line}{" "*offset}*")
                
                else:
                    print(f"*{" "*offset}{scraped_line}{" "*((max_width-len(scraped_line)+offset))}*")


                    


                if len(result_string) < max_width-1:
                   create_edges(max_width,offset)
                   return None
            
                result = wrap_line(result_string[max_width:])

                return result
        
            print(create_edges(max_width,offset))
            wrap_line(str(result))
            print(create_edges(max_width,offset))
        
            return None
        return wrapper
    return decorator


