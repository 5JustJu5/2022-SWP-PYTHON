import java.util.ArrayList;
import java.util.List;

public class KWetterstation implements Wetterstation {

	List<Bildschirme> beobachterList = new ArrayList();
	
	int state = 0;
	
	@Override
	public void addBeobachter(Bildschirme beobachter) {
		this.beobachterList.add(beobachter);
	}

	@Override
	public void removeBeobachter(Bildschirme beobachter) {
		this.beobachterList.remove(beobachter);
	}

	@Override
	public void notifyAlleBeobachter() {
		for (Bildschirme beobachter : beobachterList) {
			beobachter.update();
		}
	}

	public int getState() {
		return state;
	}

	public void setState(int state) {
		this.state = state;
		this.notifyAlleBeobachter();
	}
}