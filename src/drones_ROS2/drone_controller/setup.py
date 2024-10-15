from setuptools import find_packages, setup

package_name = 'drone_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jagadeesh',
    maintainer_email='rachapudijagadeesh9580@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'img_sub = drone_controller.img_sub:main',
        	'image_sub = drone_controller.image_sub:main',
        	'image_pub = drone_controller.image_pub:main',
        	'img_sub2 = drone_controller.img_sub2:main',
        	'img_sub3 = drone_controller.img_sub3:main',
            'pose_sub = drone_controller.pose_sub:main',
 #           'img_sub2 = drone_controller.img_sub2:main'
        ],
    },
)
