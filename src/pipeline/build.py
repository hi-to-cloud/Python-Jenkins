import subprocess

class BuildPipeline:
    @staticmethod
    def run():
        print("Running build process...")
        result = subprocess.run(["echo", "Building..."], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            raise Exception("Build failed!")
