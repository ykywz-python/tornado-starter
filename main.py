import asyncio
import sys
import tornado.ioloop

import webbrowser
from src.boot import Application
from src.config.const import APP_BANNER, APP_NAME, APP_PORT, APP_URL, APP_VERSION
from src.utils.process import kill_proc_tree
from src.utils.singleton import ensure_single_instance

async def main():
    # Ensure only one instance of the application can run.
    # This must be the first call.
    ensure_single_instance(APP_NAME, APP_PORT)

    print(APP_BANNER)
    print('Version:', APP_VERSION)
    print('Port:', APP_PORT)
    print("\n")
    
    app = Application()
    
    server = None
    try:
        print('Starting server...')    
        server = app.listen(APP_PORT)
        
        print(f"Server started on host: {APP_URL}")
        webbrowser.open_new_tab(APP_URL)

        print("\n")
        
        print("Press Ctrl+C to quit")
        
        print("\n\n")

        await asyncio.Event().wait()
        
    except KeyboardInterrupt:
        print("\nCtrl+C received. Shutting down gracefully...")
    finally:
        if server:
            server.stop()
        app.shutdown()
        print("Server has been stopped. Exiting.")
        kill_proc_tree()
        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())