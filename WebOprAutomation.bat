@echo off
setlocal EnableDelayedExpansion

	if "%$ecbId%" == "" (
		:Proc1
		echo Enter '1' to Execute whole Project
		echo Enter '2' to Execute any single module
		echo Enter anything else to abort.
		echo.
		set "UserChoice=abort"
		set /P "UserChoice=Type input: "

 		if "!UserChoice!"=="1" (
			pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests
 		)
		)


		if "!UserChoice!"=="2" (

			:Proc2
			echo Single Modules List
			echo Enter '3' to Execute Server login
			echo Enter '4' to Execute Attorney
			echo Enter '5' to Execute Server system settings
			echo Enter '6' to Execute Server SMNP settings
			echo Enter '7' to Execute Server Node Management
			echo Enter '8' to Execute Server Packetizer configuration
			echo Enter '9' to Execute Server TrunkGroup
			echo Enter '10' to Execute Server Users
			echo Enter 'a' to Execute single TCs

			echo Enter anything else to abort
			echo Enter 'r' to return main menu
			echo.
			set "UserChoice=abort"
			set /P "UserChoice=Type input: "

			if "%$ecbId%" == "" (

				if "!UserChoice!"=="3" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests\LoginTCs.py
					goto :Proc2
				)
				if "!UserChoice!"=="4" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests\TestAttorneys.py
					goto :Proc2
				)
				if "!UserChoice!"=="5" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests\test_05_server_system_configuration.py
					goto :Proc2
				)
				if "!UserChoice!"=="6" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests\test_06_SNMPSettings.py
					goto :Proc2
				)
				if "!UserChoice!"=="7" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests\test_07_Nodes.py
					goto :Proc2
				)
				if "!UserChoice!"=="8" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests\test_08_Packetizer.py
					goto :Proc2
				)
				if "!UserChoice!"=="9" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests\test_09_TrunkGroup.py
					goto :Proc2
				)
				if "!UserChoice!"=="10" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests\test_10_ServerUser.py
					goto :Proc2
				)

				if "!UserChoice!"=="99" (
					pytest -rA --html=.\reports\Report_"%date:~0,2%%date:~3,2%%date:~6,4%"_"%time:~0,2%%time:~3,2%%time:~6,2%".html "%CD%\Tests\test_99_TestCasesSheetEmail.py
					goto :Proc2
				)
				if "!UserChoice!"=="r" (
					goto :Proc1
				)
			)
		)

            if "!UserChoice!"=="r" (
					goto :Proc2
				)
        )

		if not "!UserChoice!"=="1" (
			if not "!UserChoice!"=="2" (
				if not "!UserChoice!"=="3" (
				    if not "!UserChoice!"=="4" (
				            if not "!UserChoice!"=="5" (
                                if not "!UserChoice!"=="6" (
                                    if not "!UserChoice!"=="7" (
                                        if not "!UserChoice!"=="8" (
                                            if not "!UserChoice!"=="9" (
                                                if not "!UserChoice!"=="10" (
                                                    if not "!UserChoice!"=="99" (
                                                    echo Unknown input ... Aborting script
                                                    timeout 5
                                                    exit /B 500

                                                )
                                            )
                                        )
                                    )

                                )
                            )
                        )
                    )
                )
            )
        )
    )
)

endlocal
pause