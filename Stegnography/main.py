import functions as fun
import pyfiglet
from rich.console import Console
import easygui
import time

console = Console()

intro1 = pyfiglet.figlet_format("IMG", font = "isometric1" )
intro2 = pyfiglet.figlet_format("S E C R E T", font = "digital" ) 
welcome = pyfiglet.figlet_format("Welcome to", font = "bubble" ) 

print(welcome)
print(intro1, intro2)

def startencode():
    data = console.input("[cyan]Enter the data that need to be hidden : [/cyan]")
    path = console.input("[yellow]Enter the path of the image : [/yellow]")
    with console.status("[bold green]Encoding data into image",spinner="aesthetic", speed= 5.0) as status:
        encoder = fun.encode(data=data,source=path)
        time.sleep(1)
        if encoder != None:
            console.print(f"[red]{encoder}[/red]")
        else:
            console.log("Successfully completed")
            console.log("Encoded image saved as output.png")
            return True

def startdecode():
    path = console.input("[yellow]Enter the path of the image : [/yellow]")
    with console.status("[bold green]Decoding image",spinner="aesthetic", speed= 5.0) as status:
        decoder = fun.decode(source=path)
        if decoder != "Image not valid":
            console.log("Successfully decoded")
            print("")
            console.print(f"[magenta]The secret is = [/magenta][purple]{decoder}[/purple]")
            return True
        else:
            console.print(f"[red]{decoder}[/red]")

while True:
    choice=console.input("[green]Do you want to [/green][magenta]Encode[/magenta][green] or [/green][magenta]Decode[/magenta] [blue]:[/blue] ").lower()
    if choice == "encode":
        if startencode():
            break
    elif choice == "decode":
        if startdecode():
            break
    else:
        console.print("Enter either Encode or Decode to procede", style="bold red")
