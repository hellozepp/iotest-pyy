#sh ./inner/dirname.sh
base_dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)
export base_dir=$base_dir
source param/paramter.sh
