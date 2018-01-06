import os
import sys


BOUNDARY = "*" * 50
rename_count = 0


def get_basename(path):
    return os.path.basename(path)


def get_abs_path(parent, child):
    return os.path.join(parent, child)


def get_top_level_dirs(dir):
    root, top_level_dirs, files = os.walk(dir).next()
    return top_level_dirs


def rename_subtitle(movie_dir):
    movie_extensions = (".mp4", ".mkv", ".avi")
    subtitle_extension = ".srt"
    movie_name = None
    subtitle_name = None

    for file_name in os.listdir(movie_dir):
        if file_name.endswith(movie_extensions):
            movie_name = file_name
        if file_name.endswith(subtitle_extension):
            subtitle_name = file_name

    if movie_name is not None and subtitle_name is not None:
        movie_name = get_abs_path(movie_dir, movie_name)
        old_subtitle_name = get_abs_path(movie_dir, subtitle_name)
        new_subtitle_name = movie_name.rsplit('.', 1)[0] + subtitle_extension

        try:
            os.rename(old_subtitle_name, new_subtitle_name)
            print(
                "Renaming from %s to %s" %
                (get_basename(old_subtitle_name),
                 get_basename(new_subtitle_name)))
            global rename_count
            rename_count += 1
        except Exception as e:
            print("Error while renaming : " + str(e))


if __name__ == '__main__':
    print(BOUNDARY)
    root_movies_dir = sys.argv[1]

    top_level_dirs = get_top_level_dirs(root_movies_dir)
    top_level_dirs = [get_abs_path(root_movies_dir, dir)
                      for dir in top_level_dirs]

    for i, dir in enumerate(top_level_dirs):
        print("Processing movie : %s" % (get_basename(dir)))
        rename_subtitle(dir)
        print(BOUNDARY)

    print("Processed %s movies" % (str(i + 1)))
    print("Renamed %s subtitles" % (str(rename_count)))
    print(BOUNDARY)
