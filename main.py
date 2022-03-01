from pathlib import Path

import shutil

class OrganizeDir:
    suffix_dir = {
            '.png': 'images',
            '.PNG': 'images',
            '.jpeg': 'images',
            '.jpg': 'images',
            '.pdf': 'pdf',
            '.docx': 'word',
            '.csv': 'databace',
            '.sql': 'databace',
            '.zip': 'compressed',
            '.rar': 'compressed',
            '.deb': 'exe',
            '.app': 'exe',
            '.exe': 'exe',
            '.dmg': 'docs',
            '.mp4': 'video',
    }

    def run(self, to_organize_dir):
        self.to_organize_dir = Path(to_organize_dir).resolve()
        assert self.to_organize_dir.exists(), f'Directory "{self.to_organize_dir}" not found!'

        for path in self.to_organize_dir.iterdir():

            if path.is_dir():
                if path.name in OrganizeDir.values():
                    continue

                dest = 'directory'
                DEST_DIR = self.to_organize_dir / dest
                DEST_DIR.mkdir(exist_ok=True)
                shutil.move(str(path), str(DEST_DIR))

            elif path.is_file():
                suffix = path.suffix
                dest = OrganizeDir.get(suffix)

                if not dest:
                    continue

                DEST_DIR = self.to_organize_dir / dest
                DEST_DIR.mkdir(exist_ok=True)
                shutil.move(str(path), str(DEST_DIR))

if __name__ == '__main__':
    HOME_DIR = Path.home()
    organizer = OrganizeDir()
    organizer.run(HOME_DIR / 'Downloads')