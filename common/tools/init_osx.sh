cd $HOME
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install wget

sudo chmod 777 /usr/local/bin
brew install gcc
brew install libjpeg
brew install libtiff
brew install git

git config --global push.default simple

wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
echo "source ~/git-completion.bash" >> ~/.bashrc

sudo easy_install pip
sudo pip install virtualenv

wget http://fastdl.mongodb.org/osx/mongodb-osx-x86_64-2.4.10.tgz
tar xvfz mongodb-osx-x86_64-2.4.10.tgz
sudo mv mongodb-osx-x86_64-2.4.10/bin/* /usr/local/bin
rm -rf mongodb-osx-x86_64-2.4.10*

wget http://download.redis.io/releases/redis-2.6.17.tar.gz
tar xvzf redis-2.6.17.tar.gz
cd redis-2.6.17
make install
cd ..

# create virtualenv
cd $HOME
virtualenv $HOME/devenv
source devenv/bin/activate

# update pip just in case
pip install --upgrade pip
pip install --upgrade setuptools==2.2
$VIRTUAL_ENV/bin/easy_install "pyramid==1.4.5"
pip install gunicorn==19.3.0

echo "if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi" >> ~/.bash_profile

echo "source ~/devenv/bin/activate" >> ~/.bashrc